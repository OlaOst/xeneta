# convenience functions for loading and parsing files

from os import listdir

def getfilelist():
    files = []
    for entry in listdir('./files'):
        # TODO: also limit to only .txt files?
        if "~" not in entry and "#" not in entry:
            files.append(entry)
    return files

def parsefiles(files, wordcount):
    #wordcount = {}
    for filename in files:
        #print "loading file " + filename
        parsefile(filename, wordcount)

# TODO: might be better performance to split the whole file instead of every line separately
def parsefile(filename, wordcount):
    lines = file("./files/" + filename, 'r').readlines()
    for line in lines:
        for word in line.split():
            if word in wordcount:
                wordcount[word] += 1
            else:
                wordcount[word] = 1
