from bottle import get, post, request, run



uploadform = '''
    <form action="/upload" method="post" enctype="multipart/form-data">
        Upload file: <input name="data" type="file" />
                     <input value="upload" type="submit" />
    </form>
'''

@get('/upload') # or @route('/login')
def upload():
    return uploadform

@post('/upload') # or @route('/login', method='POST')
def do_upload():
    #name = request.forms.name
    data = request.files.data

    if data and data.file:
        raw = data.file.read() # Dangerous for big files
        filename = data.filename

        # TODO: this will overwrite any existing file, should check and give message instead of overwriting
        savefile = file("./files/" + filename, 'w')
        savefile.write(raw)
        savefile.close()

        report = "<p>The uploaded file named " + filename + " is " + str(len(raw)) + " bytes long</p>"
        report += "<p>Raw file contents are:</p><pre>" + raw + "</pre>"
    else:
        report = "<p>You missed a field or there was a problem uploading the file.</p>"

    return uploadform + report

run(host='0.0.0.0', port=8080)
