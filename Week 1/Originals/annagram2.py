


def wordcompare(x, y="steal"):
    if isinstance(x,int) or isinstance(y, int):
        print("Those are not strings")
    elif sorted(x) == sorted(y):
        print("annagram")           
    elif sorted(x) != sorted(y):
        print(x,y)
    
wordcompare("race")
print()
wordcompare("Pizza")
print()
wordcompare(1)
print()
wordcompare("least")
print()
