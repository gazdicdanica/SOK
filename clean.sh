#
# Remove all garbage produced by Django and each of the components upon installation. 
#

purge_eggs() {
    cd $1

    rm -rf build/
    rm -rf *.egg-info
    rm -rf dist/

    cd ..
}

remove_database() {
    cd kenigsberg
    rm -rf *.sqlite3
    cd ..
}

purge_eggs core
purge_eggs parse_json
purge_eggs parse_yaml
purge_eggs render_standard
purge_eggs render_classdiag
purge_eggs render_3
# ...
# don't forget to add the same commands in ./pyvenv.ps1

remove_database