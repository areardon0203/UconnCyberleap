def swaps_quad(L):
   count = 0

   for i in range(len(L)): # Take every item, and
      for j in range(i):   # compare it to every item before
         if L[i] < L[j]:
            count += 1
   
   return count

def is_sorted(L):
    return not any(L[i] > L[i+1] for i in range(len(L)-1))

def swaps(L, left=0, right=None, swap_counter=None):
    if right is None: right = len(L)

    if swap_counter is None: swap_counter = 0

    pivot = right - 1
    i, j = left, pivot - 1

    while i < j:
        while L[i] < L[pivot]: i += 1
        while L[j] >= L[pivot] and i < j: j -= 1
        if L[i] > L[j]: 
            L[i], L[j] = L[j], L[i]
            swap_counter += 1

    if L[i] >= L[pivot]:
        L[i], L[pivot] = L[pivot], L[i]
        pivot = i

    if pivot == len(L) // 2: 
        return L[pivot], swap_counter

    elif pivot > len(L) // 2:
        res, subswaps = swaps(L, left, pivot, swap_counter)
        swap_counter += subswaps
        return res, swap_counter

    elif pivot < len(L) // 2:
        res, subswaps = swaps(L, pivot+1, right, swap_counter)
        swap_counter += subswaps
        return res, swap_counter
   
assert swaps([2,1,3,6]) == 1

# print(swaps_quad([1, 2, 3])) # should be 0
# print(swaps_quad([4, 2, 3])) # should be 2: 4 is greater than 2 and 3
# print(swaps_quad([4, 3, 2])) # should be 3: 4 > 3 and 2, and 3 > 2

