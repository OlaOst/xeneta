from bottle import get, post, request, run



uploadform = '''
    <form action="/upload" method="post">
        Upload file: <input name="file" type="file" />
        <input value="upload" type="submit" />
    </form>
'''

@get('/upload') # or @route('/login')
def upload():
    return uploadform

@post('/upload') # or @route('/login', method='POST')
def do_upload():
    filedata = request.forms.get('file')
    report = "<p>The uploaded file is " + str(len(filedata)) + " bytes long</p>"
    report += "<p>File contents are:</p><p>" + filedata + "</p>"
    report +="<p>Request forms keys are: " + str(request.forms.keys()) + "</p>"
    return uploadform + report

run(host='0.0.0.0', port=8080)
