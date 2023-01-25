
import WordCompare

words = ["tar", "rat", "art", "face", "cafe", "hello"]

def find_anagrams(word): 
    '''
    First initialize an empty dictionary to store anagrams.

    Iterate over the each word and create a new dictionary for x.

    Iterate over the same list a second time as y

    Compare x and y, if x is y test if it is an anagram or the same word.

    If anagram is returned, add to anagrams list x

    Iterate over each new dictionary and return all anagram pairs.
    '''   
    anagrams = dict()
    for x in word:
        anagrams[x] = []
        for y in word:
            if x is y:
                continue
            if WordCompare.word_compare(x,y)=="anagrams":
                anagrams[x].append(y)
    
    for key, value in anagrams.items():
        return(key, value)
        
wordList=["largely", "gallery", "allergy", "alert", "alter", "later", "cow", "cat", "house", "giraffe", "pine","pizza"]

find_anagrams(wordList)
# expectedresult = []
# assert find_anagrams(wordList) == expectedresult