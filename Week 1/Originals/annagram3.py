def wordcompare(x=4, y=3):
    if not isinstance(x,str) or isinstance(y, str):
        return False
    elif sorted(x) == sorted(y):
        return 'Anagram'     
    elif sorted(x) != sorted(y):
        return False
    

wordcompare()