# Hello world hwd (mpy)

RPi Pico sandpit for first getting started code and content.

First steps in electeical engineering. First steps in MicroPython.

## Status

TODO
* <todo: consider, basic programming techniques in MicroPython, loops, text, numbers, >
* <todo: consider, create distribution package and use with pipkin for Thonny IDE, from local host, >
* <todo: consider, disable egg creation in build process, egg and egg.info are depricated and have no official standards specification, wheels in place of eggs, wheels have spec PEP 427 2012, >
* <todo: consider, iterate build section, packaging and so on, needs much more work, look at pyOpenSci in first instance for more info, seek other similar sources, >
* <todo: consider, rebuild distribution without .egg-info, try something other than PDM , try Hatch as recomended by pyOpenSci, >

DONE
* <done: consider, flash RPi Pico with MicroPython>
* <done: consider, write MicroPython code to execute on RPi Pico >
* <done: consider, first circuit in boradboard with RPi Pico >
* <done: consider, standard python distribution format, create example package, >
* <done: consider, delete egg zip directory in Github repo under /src >
* <done: consider, different build tools for different use case, map use case to build tool, at this point have no idea as to criteria for evaluaiton, pyOpenSci may point to a way ahead, need one Micropython build with C/C++ and Rust and likely other languages, wip, continued research required, pyOpenSci recommend Hatch, >

## Output

### Make a distribution package for a python project
Build Success reported, using Hatch, following instructions in the pyOpenSci site, see link below
* <info: for first begginer build ensure, confib.toml has tests=false . ensure pyproject.toml has sections; [build-system] requires = ["hatchling"] build-backend = "hatchling.build" ,  [tool.hatch.build.targets.wheel] packages = ["src/org"] .>
* <todo: recreate venv for /hwd and build using hatch, include success below, >
* <todo: update /hwd pyproject.toml, to be hatch compliant, >

```
<comment; lots of output on failure, on success only the following>

(venv) C:\path\to\your\dev\project\electrical-engineering\rpi-pi\mpy\dsp>hatch build
──────────────────────────────────────────────────────── sdist ────────────────────────────────────────────────────────
dist\display_org_agw_een_dsp-0.0.1.tar.gz
──────────────────────────────────────────────────────── wheel ────────────────────────────────────────────────────────
dist\display_org_agw_een_dsp-0.0.1-py3-none-any.whl

```

## Lib
<todo: still confussed by Frontend and Backend tool differences, this section needs reworking >

### Build Frontend 
Package Manager - python package manager, not linux system package manager,
Finding it difficult to distinguish between frontend and backend, build ecosystem

Lists - info 
* list of packaging managers, python org [WS](https://packaging.python.org/en/latest/key_projects/), 
* Python Package Guide, pyOpenSci [WS](https://www.pyopensci.org/python-package-guide/index.html), Investigate more, very interesting! 

Products
* Build, [WS](https://packaging.python.org/en/latest/key_projects/#build), not a package manager a build system, <todo: to be recategorized >
* Pip, 
* Pipkin, [WS](https://pypi.org/project/pipkin/), Thonny IDE uses this under the hood, to create local packages for RPi Pico MicroPython env, e.g. BYO drivers for periferal devices, sensors, screens,  
* Python Packaging User Guide, [WS](https://packaging.python.org/en/latest/), 
* Python Packaging Authority, [WS](https://www.pypa.io/en/latest/)
* Overview of Python Packaging, [WS](https://packaging.python.org/en/latest/overview/)

### Build Backend

* Flit core, 
* Hatch, pypi [WS](https://pypi.org/project/hatch/), pypa [WS](https://hatch.pypa.io/latest/), pyOpenSci get to know hatch [WS](https://www.pyopensci.org/python-package-guide/tutorials/get-to-know-hatch.html), pip install hatch
* Hatchling, pypi [WS](https://pypi.org/project/hatchling/), Note this did not work <todo: consider, deleting this listing entry>
* meson-python
* PDM, pypi [WS](https://pypi.org/project/pdm/), org [WS](https://pdm-project.org/en/latest/), [GH](https://github.com/pdm-project/pdm), 
* scikit-build-core, 
* Setuptools

## Notes

### Make a distribution package for a python project

Open a command prompt - e.g. Thonny IDE>Tools>Open system shell ...
* navigate to the project directory of interest
* the project directory contains the; /src directory, README.md  file, pyproject.toml file, and so on ...

Create a project specific Python environment instance - to contain for example project dependencies and build specific requirements
* python -m venv venv , Windows - this only has to be done once
* venv\Scripts\activate , Windows - do this for every new cmd shell
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
* Modules, [WS](https://docs.python.org/3/tutorial/modules.html#), 
* Python Package, formats [WS](https://packaging.python.org/en/latest/discussions/package-formats/#package-formats), not Linux Distribution package, not distro package, 
* Python Package, Python Import Format, [WS](https://packaging.python.org/en/latest/glossary/#term-Import-Package), import package, 
* Python Package, Python Distribution Format, [WS](https://packaging.python.org/en/latest/specifications/binary-distribution-format/), distribution package, 
* source distributions (sdists), source distribution compressed archive, 
* binary distributions (wheels), binary distribution wheels,
* file, ```__init__.py```, add to every code package directory before build, otherwise will generate an ImportError: no module named
* file, pyproject.toml, standard source distribution, Writing your pyproject.toml, [WS](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#writing-pyproject-toml)
* file, PKG-INFO, metadata file, core metadata, [WS](https://packaging.python.org/en/latest/specifications/core-metadata/#core-metadata)
* file, name, sdist, .tar.gz or .zip file extension, example; pip-23.3.1.tar.gz , {name}-{version}.tar.gz, posix tarball, POSIX.1-2001 pax tar format, utf8 file name,
* file, name, bdist, .whl file extension, example; pip-23.3.1-py3-none-any.whl , 
* file, depricated, setup.py, [WS](https://packaging.python.org/en/latest/discussions/setup-py-deprecated/), depricate as python command use, not depricated for use with Setuptools, 
* file, depricated, <some-compressed-file-name>.egg-info, [WS](https://packaging.python.org/en/latest/discussions/package-formats/#what-about-eggs), Setuptools, no official standard specification PEP
* variable, PYTHONPATH, environment variable

News Papers - getting started
* Raspberry Pi Pico Getting Started Guide, [WS](https://thepihut.com/blogs/raspberry-pi-tutorials/raspberry-pi-pico-getting-started-guide), 19 Dec 2022, The Pi Hut,

 Standard Python distribution format - build issues
* ERROR Backend subproccess exited when trying to invoke get_requires_for_build_sdist, [WS](https://stackoverflow.com/questions/72072319/error-backend-subproccess-exited-when-trying-to-invoke-get-requires-for-build-sd), StackOverflow, 
* ERROR Backend subprocess exited when trying to invoke get_requires_for_build_sdist #572, [WS](https://github.com/pypa/build/issues/572), GitHub, pypa, 
* ERROR Backend subprocess exited when trying to invoke get_requires_for_build_sdist, [WS](https://stackoverflow.com/questions/75312569/error-backend-subprocess-exited-when-trying-to-invoke-get-requires-for-build-sdi), StackOverflow, 
* ...

News Papers - execution of code from another package, path, directory
* Run Script From Another Directory in Python, [WS](https://codeigo.com/python/run-script-from-another-directory/), Codegio, 
* How to execute a python script in a different directory?, [WS](https://stackoverflow.com/questions/45384429/how-to-execute-a-python-script-in-a-different-directory), StackOverflow, 

News Papers - markup, code block
*  Fenced Code Blocks [WS](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks)



