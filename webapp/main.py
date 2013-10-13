# main webapp entry point

from bottle import run, route, static_file
import displayfiles
import displayfile


@route('/js/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./js/')

run(host='0.0.0.0', port=8080)
