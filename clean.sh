#
# Remove all garbage produced by Django and each of the components upon installation. 
#

purge-eggs() {
    cd $1

    rm -rf build/
    rm -rf *.egg-info
    rm -rf dist/

    cd ..
}

remove-database() {
    cd kenigsberg
    rm -rf *.sqlite3
    cd ..
}

purge-eggs core
purge-eggs parse_json
# purge-eggs plugin2
# ...
# don't forget to add the same commands in ./pyvenv.ps1

remove-database