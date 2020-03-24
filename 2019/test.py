
import re

def shortestPath(document, word1, word2):

    words = re.split(" ", document)
    print(words)

    for word in words:





document = "This is a sample document we just made up"
word1 = "sample"
word2 = "document"

shortestPath(document, word1, word2)