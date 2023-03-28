def is_sorted(L):
    return not any(L[i] > L[i+1] for i in range(len(L)-1))

def mergesort(L):
    #base case
    if len(L) <= 1: return L

    median = len(L) // 2
    left = L[:median]
    right = L[median:]

    left = mergesort(left)
    right = mergesort(right)

    #Start zipping up subproblems

    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L[i+j] = left[i]
            i += 1
        
        else:
            L[i+j] = right[j]
            j+=1
    #add remaining sublist items to L
    L[i+j:] = left[i:] + right[j:]

    #return list to next level of recursion
    return L

#Create an unsorted list, then sort it

if __name__ == '__main__':
    import random 
    L = [random.randint(0,10) for i in range(10)]
    L.append(-1)

    #sort it

    assert(not is_sorted(L))
    mergesort(L)
    print(L)
    assert(is_sorted(L))
   