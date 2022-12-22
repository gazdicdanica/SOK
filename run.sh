#
# Install all of the components and run the server.
# You may want to consider running `clean` beforehand.
#

lay-eggs() {
    pip install $1/
}

run-server() {
    python kenigsberg/manage.py makemigrations
    python kenigsberg/manage.py migrate
    python kenigsberg/manage.py runserver
}

lay-eggs core
lay-eggs parse_json
lay-eggs render_json
lay-eggs render_standard
lay-eggs render_classdiag
lay-eggs render_3
# ...
# don't forget to add the same commands in ./pyvenv.ps1

run-server