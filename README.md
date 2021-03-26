# instawow-installer

Dirty script to automate pulling and placement of the [instawow](https://github.com/layday/instawow) CLI and GUI components (Windows NT only).

## Requirements

- Python v3.9+
  - `requests`

Building additionally requires:

- `pyinstaller`
- [7zip](https://www.7-zip.org/) (installed to `%PATH%`)

## Installation

Unzip the contents of `instawow-installer.zip`.

## Usage

Edit `dl.cfg` to set the installation directory ('`install_dir`') to somewhere on your `%PATH%`.
