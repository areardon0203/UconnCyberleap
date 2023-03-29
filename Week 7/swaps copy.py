def swaps_quad(L):
   count = 0

   for i in range(len(L)): # Take every item, and
      for j in range(i):   # compare it to every item before
         if L[i] < L[j]:
            count += 1
   
   return count

def is_sorted(L):
    return not any(L[i] > L[i+1] for i in range(len(L)-1))

def swaps(L, swap_count=None):
    if swap_count == None: swap_count = 0
    #base case
    if len(L) <= 1: return swap_count

    median = len(L) // 2
    left = L[:median]
    right = L[median:]

    swap_count = swaps(left, swap_count)
    swap_count = swaps(right, swap_count)

    #Start zipping up subproblems

    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L[i+j] = left[i]
            i += 1
        
        else:
            L[i+j] = right[j]
            swap_count += 1
            j+=1
    #add remaining sublist items to L
    L[i+j:] = left[i:] + right[j:]

    #return list to next level of recursion
    return swap_count
   
x = [2,1,4,3]
print(x)
p = swaps(x)
print(p)