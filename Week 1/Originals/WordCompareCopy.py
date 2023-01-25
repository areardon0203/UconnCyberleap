def word_compare(x, y):
    if not (isinstance(x,str) and isinstance(y, str)):
        return False
    elif sorted(x) == sorted(y):
        return 'anagrams'          
    elif sorted(x) != sorted(y):
        return False
    