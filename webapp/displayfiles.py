from bottle import route, view, run
from fileutil import getfilelist, parsefiles

@route('/display')
@view('display')
def display():
    result = {}

    # TODO: time this for large files and with multiple simultaneous connections and optimize if needed
    files = getfilelist()

    #print "got files: " + str(files)
    #result = "<p>Files loaded: " + ", ".join(files) + "</p>"
    result['files'] = ", ".join(files)

    # TODO: make global wordcount so we do not have to recalculate it from all files on every request
    wordcount = {}
    parsefiles(files, wordcount)

    sortedwords = sorted(wordcount, key=wordcount.get, reverse=True)

    #result += "<p>20 most popular words:</p><p>"
    topwords = ""
    for word in sortedwords[:20]:
        topwords += word + ": " + str(wordcount[word]) + "<br/>"

    result['topwords'] = sortedwords[:20]

    return result
