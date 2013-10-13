from bottle import route, view, run
from fileutil import getfilelist, parsefiles

@route('/displayfiles')
@view('displayfiles')
def displayfiles():
    result = {}

    files = getfilelist()

    #filelinks = []
    #for filename in files:
    #    filelinks.append("<a href='/displayfile/" + filename + "'>" + filename + "</a>")

    #result['files'] = ", ".join(files)
    result['files'] = files

    # TODO: make global wordcount so we do not have to recalculate it from all files on every request
    #wordcount = {}
    #parsefiles(files, wordcount)

    #sortedwords = sorted(wordcount, key=wordcount.get, reverse=True)

    #topwords = ""
    #for word in sortedwords[:20]:
    #    topwords += word + ": " + str(wordcount[word]) + "<br/>"

    #result['topwords'] = sortedwords[:20]
    #result['wordcounts'] = [wordcount[word] for word in sortedwords[:20]]

    return result

@route('displayfiles', method='POST')
@view('displayfiles')
def do_upload():
    data = request.files.data

    if data and data.file:
        raw = data.file.read() # Dangerous for big files
        filename = data.filename

        # TODO: this will overwrite any existing file, check and give message instead of overwriting?
        savefile = file("./files/" + filename, 'w')
        savefile.write(raw)
        savefile.close()

        files = getfilelist()
        result['files'] = ", ".join(files)

        return result
