## PythonColorize [![Build Status](https://travis-ci.org/TiagoDanin/PythonColorize.svg?branch=master)](https://travis-ci.org/TiagoDanin/PythonColorize) [![GPLv3](https://img.shields.io/aur/license/yaourt.svg?maxAge=2592000)](https://github.com/TiagoDanin/PythonColorize/blob/master/LICENSE) [![Pypi](https://img.shields.io/badge/PythonColorize-Pypi-yellow.svg)](https://pypi.python.org/pypi/PythonColorize)
**Simple module to colorize text on terminal :D**

## Requires
Written for Python3.x

But work with python2.X

## Setup
Open terminal:

`git clone https://github.com/TiagoDanin/PythonColorize.git`

`sudo python3 setup.py install`

or via pip:

`sudo pip3 install PythonColorize`

## DOC

Colors  | Styles    |
--------|-----------|
black   | bold      |
red     | dark      |
green   | underline |
yellow  | negative  |
blue    | hide      |
magenta |           |
cyan    |           |
white   |           |

Module function:

- Get color `PythonColorize.colors.<[param][style]_>[name]`

> <.> Optional


 Params | Option     |
--------|------------|
lg_     | light      |
bg_     | background |


- Colorize `PythonColorize.colorize(text=[text], color=[color], style=[style], light=[True|False])`

## Pages
Module [File](https://github.com/TiagoDanin/PythonColorize/blob/master/PythonColorize.py)

Example [File](https://github.com/TiagoDanin/PythonColorize/blob/master/example.py)

Suggestions and Support [New Issue](https://github.com/TiagoDanin/PythonColorize/issues/new)

For stable versions to access [Releases](https://github.com/TiagoDanin/PythonColorize/releases)


## LICENSE
GNU General Public License v3 [(GPLv3)](https://github.com/TiagoDanin/PythonColorize/blob/master/LICENSE)

---
>Copyright (c) 2016 Tiago Danin
