from bottle import get, run
from fileutil import getfilelist, parsefiles

@get('/display')
def display():
    # TODO: time this for large files and with multiple simultaneous connections and optimize if needed
    files = getfilelist()

    #print "got files: " + str(files)
    result = "<p>Files loaded: " + ", ".join(files) + "</p>"

    # TODO: make global wordcount so we do not have to recalculate it from all files on every request
    wordcount = {}
    parsefiles(files, wordcount)

    sortedwords = sorted(wordcount, key=wordcount.get, reverse=True)

    result += "<p>20 most popular words:</p><p>"
    for word in sortedwords[:20]:
        result += word + ": " + str(wordcount[word]) + "<br/>"

    return result
