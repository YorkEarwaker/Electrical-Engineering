# Hello world hwd (mpy)

RPi Pico sandpit for first getting started code and content.

First steps in electeical engineering. First steps in MicroPython.

## Status

TODO
* <todo: consider, basic programming techniques in MicroPython, loops, text, numbers, >
* <todo: consider, standard python distribution format, package, use with pipkin for Thonny IDE, from local host, >

DONE
* <done: consider, flash RPi Pico with MicroPython>
* <done: consider, write MicroPython code to execute on RPi Pico >
* <done: consider, first circuit in boradboard with RPi Pico >

## Lib

### Build Frontend
Package Manager - python package manager, not linux system package manager

* Build, [WS](https://packaging.python.org/en/latest/key_projects/#build), 
* Pip, 
* Pipkin, [WS](https://pypi.org/project/pipkin/), Thonny IDE uses this under the hood, to create local packages for RPi Pico MicroPython env, e.g. BYO drivers for periferal devices, sensors, screens,  
* Python Packaging User Guide, [WS](https://packaging.python.org/en/latest/), 
* Python Packaging Authority, [WS](https://www.pypa.io/en/latest/)
* Overview of Python Packaging, [WS](https://packaging.python.org/en/latest/overview/)

### Build Backend

* Flit core, 
* Hatchling,
* meson-python
* PDM
* scikit-build-core
* Setuptools

## Notes

### Make a distribution package for a python project

Create a project specific Python environment instance - to contain for example project dependencies and build specific requirements
* python -m venv venv , Windows
* venv\Scripts\activate , Windows
* source venv/bin/activate , Unix/MacOS
* ...<do some stuff in the new python project env, >
* deactivate

Get the latest version of pip
* python3 -m pip install --upgrade pip , Unix/MacOS
* py -m pip install --upgrade pip , Windows

Get the latest verion of build
* python3 -m pip install --upgrade build , Unix/macOS
* py -m pip install --upgrade build , Windows

Commnad line to generate build - from dircectory that contains the pyproject.toml file
* python3 -m build , Unix/MacOS
* py -m build , Windows

## Reference

Terms
* Build Backend, Python org [WS](https://packaging.python.org/en/latest/glossary/#term-Build-Backend), 
* Build Frontend, Python org [WS](https://packaging.python.org/en/latest/glossary/#term-Build-Frontend), 
* Classifiers, [WS](https://pypi.org/classifiers/), list of classifers, for pyproject.toml files, python package metadata, 
* Python Package, not Linux Distribution package, not distro package, 
* Python Package, Python Import Format, import package, 
* Python Package, Python Distribution Format, distribution package, 
* source distributions (sdists), source distribution compressed archive, 
* binary distributions (wheels), binary distribution wheels,
* file, setup.py, 
* file, pyproject.toml, standard source distribution, [WS](Writing your pyproject.toml)
* file, PKG-INFO, metadata file, core metadata, [WS](https://packaging.python.org/en/latest/specifications/core-metadata/#core-metadata)
* file, name, sdist, .tar.gz or .zip file extension, example; pip-23.3.1.tar.gz , {name}-{version}.tar.gz, posix tarball, POSIX.1-2001 pax tar format, utf8 file name,
* file, name, bdist, .whl file extension, example; pip-23.3.1-py3-none-any.whl , 

News Papers - getting started
* Raspberry Pi Pico Getting Started Guide, [WS](https://thepihut.com/blogs/raspberry-pi-tutorials/raspberry-pi-pico-getting-started-guide), 19 Dec 2022, The Pi Hut,

 Standard Python distribution format
* 

News Papers - execution of code from another package, path, directory
* Run Script From Another Directory in Python, [WS](https://codeigo.com/python/run-script-from-another-directory/), Codegio, 
* How to execute a python script in a different directory?, [WS](https://stackoverflow.com/questions/45384429/how-to-execute-a-python-script-in-a-different-directory), StackOverflow, 

News Papers - markup, code block
*  Fenced Code Blocks [WS]{https://www.markdownguide.org/extended-syntax/#fenced-code-blocks)



