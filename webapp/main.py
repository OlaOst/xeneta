# main webapp entry point

from bottle import run
import displayfiles
import fileupload

run(host='0.0.0.0', port=8080)
