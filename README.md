# instawow-installer

Dirty script to automate pulling and placement of the [instawow][1] CLI and GUI components on Windows.

[1]: https://github.com/layday/instawow

## Installation

See the [releases page](https://github.com/onoira/instawow-installer/releases).

## Usage

Edit `dl.cfg` to set the installation directory ('`install_dir`') to somewhere on your `%PATH%`, then run `dl.exe`.

## Building

Requirements:

- Python 3.9
- `requests~=2.25.0`
- `py2exe~=0.10.1.0`
- [7zip](https://www.7-zip.org/) installed on your `%PATH%`.
- pwsh

Run `build.ps1`. The application will be inside the `dist/` directory.

## Contributing

This repository is not open for contributions.

Please [create a new issue](https://github.com/onoira/instawow-installer/issues/new).

## License

[MIT](LICENSE)
