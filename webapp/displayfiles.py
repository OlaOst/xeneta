from bottle import get, run

@get('/display')
def display():
    examplefile = file("files/example.txt", 'r')
    lines = examplefile.readlines()

    # TODO: time this for large files and with multiple simultaneous connections and optimize if needed
    wordcount = {}
    for line in lines:
        for word in line.split():
            if word in wordcount:
                wordcount[word] += 1
            else:
                wordcount[word] = 1

    return str(wordcount)

run(host='0.0.0.0', port=8080)
