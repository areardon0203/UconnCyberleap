import annagram3

words = ["tar", "rat", "art", "face", "cafe", "hello"]

for x in words:
    for y in words:
        if x is y:
            break
        elif annagram3.wordcompare(x,y):
            print(x,y)
        

