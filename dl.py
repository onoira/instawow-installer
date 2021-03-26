from __future__ import annotations

import json
import os
import os.path as path
import re
import shutil
import zipfile
from configparser import ConfigParser
from glob import glob

import requests

_RE_NAME_GUI = re.compile(
    r'\b\binstawow-desktop.+\.exe\b',
    flags=re.IGNORECASE
)
_RE_NAME_CLI = re.compile(
    r'\binstawow-(?:cli-)?windows.+\.zip\b',
    flags=re.IGNORECASE
)

DOWNLOAD_DIRECTORY = './download'
REPO_PATH = "layday/instawow"


class GitHubClient():

    def get_asset(self, url: str) -> bytes:
        return self._get(url).content

    def get_manifest(self, repo_path: str) -> dict:
        owner, repo = repo_path.split('/')
        resp = self._get(
            f'https://api.github.com/repos/{owner}/{repo}/releases/latest'
        )
        jso = json.loads(resp.content)
        return jso

    def _get(self, url):
        return requests.get(url, headers=self.headers)

    def __init__(self, headers: dict = None):
        self.headers = {
            'Accept': "application/vnd.github.v3+json"} | (headers or dict())


def collect_assets(assets: list[dict]) -> dict[str, str]:
    assets = {
        'instawow-gui.exe': next(
            i['browser_download_url'] for i in assets if _RE_NAME_GUI.match(i['name'])
        ),
        '.instawow.zip': next(
            i['browser_download_url'] for i in assets if _RE_NAME_CLI.match(i['name'])
        )
    }
    return assets


def download_assets(
    client: GitHubClient,
    assets: list[dict[str, str]],
    download_dir: str
) -> None:
    for name, url in assets.items():
        file = path.join(download_dir, name)

        print(f"Downloading '{url}' (-> {file})...")

        content = client.get_asset(url)
        with open(path.join(download_dir, name), 'wb') as fp:
            fp.write(content)

        if name.endswith('.zip'):
            print(f"Unzipping '{file}' (-> {download_dir})")
            with zipfile.ZipFile(file, 'r') as zr:
                zr.extractall(download_dir)


def copy_assets(
    files: list[str],
    download_dir: str,
    install_dir: str
) -> None:
    for src in files:
        dst = path.join(install_dir, path.basename(src))

        if path.exists(dst):
            print(f"Backing up '{dst}'")
            shutil.move(dst, dst + '.bak')

        print(f"Copying '{src}' -> '{dst}'")
        shutil.copy(src, dst)


def main():

    config = ConfigParser()
    config.read('dl.cfg')

    install_dir = config['default']['install_dir']
    print(f"Using install directory '{install_dir}'")

    download_dir = path.abspath(DOWNLOAD_DIRECTORY)
    if not path.exists(download_dir):
        print(f"Creating directory '{download_dir}'")
        os.makedirs(download_dir)

    client = GitHubClient()

    manifest = client.get_manifest(REPO_PATH)

    version = manifest['tag_name']
    print(f"Collecting instawow-{version}...")

    assets = collect_assets(manifest['assets'])
    download_assets(client, assets, download_dir)

    files = [i for i in glob(path.join(download_dir, '*.exe'))]
    copy_assets(files, download_dir, install_dir)

    print("Done.")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
