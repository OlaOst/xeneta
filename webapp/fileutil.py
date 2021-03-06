# convenience functions for loading and parsing files

from os import listdir
from re import sub
from memoize import memoize
import codecs


def getfilelist():
    '''Get list of filenames from ./files directory
       filters out tmp files containing ~ and # in their filenames
    '''
    files = []
    for entry in listdir('./files'):
        # TODO: also limit to only .txt files?
        if "~" not in entry and "#" not in entry:
            files.append(entry)
    return files


#@memoize
def parsefile(filename, wordcount):
    '''Loads file from filename in ./files/ directory
       Split into words excluding some common words and one-letter strings,
       and fill a dictionary where keys are words and values are the count of
       the words. The dictionary is passed as a parameter, not returned.
    '''
    content = file("./files/" + filename, 'r').read()
    #content = codecs.open("./files/" + filename, "r", "utf-8").read()

    washedcontent = sub('[^a-zA-Z\'_]', ' ', content).lower()

    excludedwords = ['the', 'an', 'a', 'of', 'in', 'at', 'and', 'or', 'to', 'his', 'hers', 'its', 'their', 'by']

    for word in washedcontent.split():
        encodedword = word.encode('utf8')
        if encodedword not in excludedwords and len(encodedword) > 1:
            if encodedword in wordcount:
                wordcount[encodedword] += 1
            else:
                wordcount[encodedword] = 1
