# convenience functions for loading and parsing files

from os import listdir

def getfilelist():
    files = []
    for entry in listdir('./files'):
        if "~" not in entry and "#" not in entry:
            files.append(entry)
    return files

# TODO: parsing all files for every page request is bad performance
# make wordcount more global and a function that appends to it for one file
# should wordcount then be defined here or where parsefiles is called?
def parsefiles(files):
    wordcount = {}
    for filename in files:
        #print "loading file " + filename
        lines = file("./files/" + filename, 'r').readlines()
        for line in lines:
            for word in line.split():
                if word in wordcount:
                    wordcount[word] += 1
                else:
                    wordcount[word] = 1
    
    return wordcount
