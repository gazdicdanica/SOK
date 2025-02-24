#
# Install all of the components and run the server.
# You may want to consider running `clean` beforehand.
#

function Lay-Eggs {
    param ($Component)

    # This is much better than `python $Component/setup.py install`
    pip install $Component/
}

function Run-Server {
    # Don't do cd because if we exit with CTRL-BREAK it will 
    # leave us at the kenigsberg/ directory instead of root.
    python kenigsberg/manage.py makemigrations
    python kenigsberg/manage.py migrate
    python kenigsberg/manage.py runserver
}

Lay-Eggs core
Lay-Eggs parse_json
Lay-Eggs parse_yaml
Lay-Eggs render_standard
Lay-Eggs render_classdiag
Lay-Eggs render_3
# ...
# don't forget to add the same commands in ./pyvenv.sh

Run-Server