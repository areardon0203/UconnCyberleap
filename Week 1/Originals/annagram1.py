def wordcompare(x, y):
    if isinstance(x,int) or isinstance(y, int):
        print("Those are not strings")
    elif sorted(x) == sorted(y):
        print("annagram")           
    elif sorted(x) != sorted(y):
        print(x,y)
    
wordcompare("race","care")
print()
wordcompare("Pizza", "bikes")
print()
wordcompare(1, "Sweet")
print()