f = open('Rainbows.txt','r')
from collections import Counter
def word_count(textFile):
        with open(textFile) as f:
                return Counter(f.read().split())
print("Number of words in the file :",word_count("Rainbows.txt"))
