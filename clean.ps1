#
# Remove all garbage produced by Django and each of the components upon installation. 
#

function RMRF-Safe {
    param ($Path)

    if (Test-Path $Path) {
        Remove-Item -Recurse -Force $Path
    }
}

function Purge-Eggs {
    param ($Component)

    cd $Component
    
    RMRF-Safe build/
    RMRF-Safe *.egg-info
    RMRF-Safe dist/

    cd ..
}

function Remove-Database {
    cd kenigsberg
    RMRF-Safe *.sqlite3
    cd ..
}

Purge-Eggs core
# Purge-Eggs plugin1
# Purge-Eggs plugin2
# ...

Remove-Database