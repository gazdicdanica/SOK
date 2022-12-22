#
# Set up a Python virtual environment and install all dependencies. 
#

function Start-Venv {
    python -m venv venv
    venv/Scripts/Activate.ps1

    python -m pip install --upgrade pip
    pip install Django
    pip install pyYAML
    # Don't forget to add the same dependency in ./pyvenv.sh

    pip list
}

Start-Venv