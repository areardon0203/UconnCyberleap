def word_compare(x=10, y="pie"):
    '''The first if statement checks if both arguments are strings.
    
    The second elif statement arranges the letters alphabetically and then compares if the two strings are equal.

    The last elif statement checks if the sorted arguments are not equal.
    '''
    if not (isinstance(x,str) and isinstance(y, str)):
        return "Those aren't strings"
    elif sorted(x) == sorted(y):
        return "anagrams"         
    elif sorted(x) != sorted(y):
        return "Those aren't anagrams"
    