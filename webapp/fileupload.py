from bottle import get, post, request, run

@get('/upload') # or @route('/login')
def upload():
    return '''
        <form action="/upload" method="post">
            Upload file: <input name="file" type="file" />
            <input value="upload" type="submit" />
        </form>
    '''

@post('/upload') # or @route('/login', method='POST')
def do_upload():
    filedata = request.forms.get('file')
    report = "<p>The uploaded file is " + str(len(filedata)) + " bytes long</p>"
    report += "<p>File contents are:</p><p>" + filedata + "</p>"
    return report

run(host='localhost', port=8080)
