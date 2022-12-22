#!/bin/bash

#
# Set up a Python virtual environment and install all dependencies. 
#

# Make sure to run it as 'source ./pyvenv.sh' so that the shell you're
# using switches to the venv that was just created!

start_venv() {
    rm -rf venv
    python -m venv venv
    source venv/Scripts/activate

    python -m pip install --upgrade pip
    python -m pip install Django
    python -m pip install pyYAML
    # Don't forget to add the same dependency in ./pyvenv.ps1

    python -m pip list 
}

start_venv