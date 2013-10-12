from bottle import get, run
from fileutil import getfilelist, parsefiles

@get('/display')
def display():
    examplefile = file("files/example.txt", 'r')
    lines = examplefile.readlines()

    # TODO: time this for large files and with multiple simultaneous connections and optimize if needed
    files = getfilelist()

    print "got files: " + str(files)

    wordcount = parsefiles(files)

    return str(wordcount)

run(host='0.0.0.0', port=8080)
