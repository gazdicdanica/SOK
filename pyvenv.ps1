#
# Set up a Python virtual environment and install all dependencies. 
#

function Start-Venv {
    python -m venv venv
    venv/Scripts/Activate.ps1

    pip install Django
    pip install pyYAML

    pip list
}

Start-Venv