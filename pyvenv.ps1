#
# Set up a Python virtual environment and install all dependencies. 
#

function RMRF-Safe {
    param ($Path)

    if (Test-Path $Path) {
        Remove-Item -Recurse -Force $Path
    }
}

function Start-Venv {
    RMRF-Safe venv
    python -m venv venv
    venv/Scripts/Activate.ps1

    python -m pip install --upgrade pip
    pip install Django
    pip install pyYAML
    # Don't forget to add the same dependency in ./pyvenv.sh

    pip list
}

Start-Venv