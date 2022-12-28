#
# Install all of the components and run the server.
# You may want to consider running `clean` beforehand.
#

lay_eggs() {
    python -m pip install $1/
}

run_server() {
    python kenigsberg/manage.py makemigrations
    python kenigsberg/manage.py migrate
    python kenigsberg/manage.py runserver
}

lay_eggs core
lay_eggs parse_json
lay_eggs parse_yaml
lay_eggs render_standard
lay_eggs render_classdiag
lay_eggs render_3
# ...
# don't forget to add the same commands in ./pyvenv.ps1

run_server