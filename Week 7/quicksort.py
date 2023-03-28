def is_sorted(L):
    return not any(L[i] > L[i+1] for i in range(len(L)-1))


def quicksort(L, left = 0, right= None):
    if right is None: right = len(L)

    if right - left <= 1: return None

    #Partitioning around a pivot

    pivot = right - 1
    i, j = left, right - 2

    #Pivot
    while i < j:
        #find first item bigger than pivot
        while L[i] < L[pivot]: i += 1
        
        while L[j] >= L[pivot] and i < j: j -= 1

        if i < j: L[i], L[j] = L[j], L[i]

    if L[i] >= L[pivot]: 
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i

    quicksort(L, left, pivot)
    quicksort(L, pivot+1, right)



if __name__ == '__main__':
    import random
    n = 100000
    L = [random.randint(0, n) for i in range(n)]
    L.append(-1)

    assert(not is_sorted(L))
    quicksort(L)
    assert(is_sorted(L))