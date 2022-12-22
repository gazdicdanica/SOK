#!/bin/bash

#
# Set up a Python virtual environment and install all dependencies. 
#

start-venv() {
    python -m venv venv
    venv/Scripts/activate

    python -m pip install --upgrade pip
    pip install Django
    pip install pyYAML
    # Don't forget to add the same dependency in ./pyvenv.ps1

    pip list 
}

start-venv