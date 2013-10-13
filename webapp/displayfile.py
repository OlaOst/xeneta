from bottle import route, view
from fileutil import parsefile


@route('/displayfile/<filename>')
@view('displayfile')
def displayfile(filename):
    result = {}

    result['file'] = filename

    # TODO: make global wordcount so we do not have to recalculate it from all
    # files on every reques. Or just memoize parsefile?
    wordcount = {}

    parsefile(filename, wordcount)

    sortedwords = sorted(wordcount, key=wordcount.get, reverse=True)

    topwords = ""
    for word in sortedwords[:20]:
        topwords += word + ": " + str(wordcount[word]) + "<br/>"

    result['topwords'] = sortedwords[:20]
    result['wordcounts'] = [wordcount[word] for word in sortedwords[:20]]

    return result
