from bottle import route, view, request
from fileutil import getfilelist, parsefiles

@route('/displayfiles')
@view('displayfiles')
def displayfiles():
    result = {}

    files = getfilelist()

    result['files'] = files

    return result

@route('/displayfiles', method='POST')
@view('displayfiles')
def displayfiles():
    result = {}

    data = request.files.data

    if data and data.file:
        raw = data.file.read() # Dangerous for big files
        filename = data.filename

        # TODO: this will overwrite any existing file, check and give message instead of overwriting?
        savefile = file("./files/" + filename, 'w')
        savefile.write(raw)
        savefile.close()

    files = getfilelist()
    result['files'] = files

    return result
