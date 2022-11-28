# Python Template
A simple template project for my python scripts.

## Project Structure
* bin - shell wrappers
* etc - configuration files
* my_app1 - module source code
* tests - test cases
* setup.py - the main setup script
* requirements.txt - dependencies

## Create a virtual environment
```
python -m venv venv
```

## Activate the virtual environment
```
# Unix
. venv/bin/activate

# PowerShell
venv\Scripts\Activate.ps1
```

## Install Wheel
```
pip install wheel
```

## Build the project
```
python setup.py build
```

## Build the Wheel distriubtion
```
python setup.py bdist_wheel
```

