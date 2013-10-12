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

    sortedwords = sorted(wordcount, key=wordcount.get, reverse=True)

    result = "<p>20 most popular words:</p><p>"
    for word in sortedwords[:20]:
        result += word + ": " + str(wordcount[word]) + "<br/>"

    #return str(wordcount)
    return result

run(host='0.0.0.0', port=8080)
