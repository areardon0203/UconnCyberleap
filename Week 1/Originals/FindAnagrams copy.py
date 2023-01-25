
import WordCompareCopy

words = ["tar", "rat", "art", "face", "cafe", "hello"]

def find_anagrams(word):
    anagrams = dict() # empty dictionary
    for x in word:
        anagrams[x] = []
        for y in word:
            if x is y:
                continue
            if WordCompareCopy.word_compare(x,y):
                anagrams[x].append(y)
    for key, value in anagrams.items():
        return (key, value)

find_anagrams(words)