import WordCompare

# list of 1st 10 ints
L = ["tar", "rat", "art", "face", "cafe", "hello"]

factors = dict() # empty dictionary

def findAnnagram(p):
    for x in p:
        factors[x] = [] # initialize to an empty list
        
        # find all numbers that cleanly divide
        for y in p:
            # if x is y:
            #     break
            if WordCompare.wordcompare(x,y):
               factors[x].append(y)
        # if x == y:
        #     factors[x].append(y)

# print out every k:v pair in dictionary
for key, value in factors.items():
    print(key, value)

print(findAnnagram(L))