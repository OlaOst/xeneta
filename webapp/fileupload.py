from bottle import get, post, request, run



uploadform = '''
    <form action="/upload" method="post" enctype="multipart/form-data">
        Upload file: <input name="name" type="text" />
                     <input name="data" type="file" />
                     <input value="upload" type="submit" />
    </form>
'''

@get('/upload') # or @route('/login')
def upload():
    return uploadform

@post('/upload') # or @route('/login', method='POST')
def do_upload():
    name = request.forms.name
    data = request.files.data

    if name and data and data.file:
        raw = data.file.read() # Dangerous for big files
        filename = data.filename
        report = "<p>The uploaded file named " + filename + " is " + str(len(raw)) + " bytes long</p>"
        report += "<p>Raw file contents are:</p><p>" + raw + "</p>"
    else:
        report = "<p>You missed a field or there was a problem uploading the file.</p>"

    return uploadform + report

run(host='0.0.0.0', port=8080)
