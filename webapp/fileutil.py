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
    for filename in files:
        parsefile(filename, wordcount)


def parsefile(filename, wordcount):
    content = file("./files/" + filename, 'r').read()

    for word in content.split():
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
