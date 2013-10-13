# convenience functions for loading and parsing files

from os import listdir
from re import sub
from memoize import memoize


def getfilelist():
    files = []
    for entry in listdir('./files'):
        # TODO: also limit to only .txt files?
        if "~" not in entry and "#" not in entry:
            files.append(entry)
    return files


def parsefiles(files, wordcount):
    for filename in files:
        parsefile(filename, wordcount)


@memoize
def parsefile(filename, wordcount):
    content = file("./files/" + filename, 'r').read()

    washedcontent = sub('[^a-zA-Z\'_]', ' ', content).lower()

    excludedwords = ['the', 'an', 'a', 'of', 'in', 'at', 'and', 'or', 'to', 'his', 'hers', 'its', 'their', 'by']

    for word in washedcontent.split():
        if word not in excludedwords:
            if word in wordcount:
                wordcount[word] += 1
            else:
                wordcount[word] = 1
