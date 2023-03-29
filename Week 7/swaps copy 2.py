def swaps(L, swap_count=None):
    if swap_count == None: swap_count = 0
    #base case
    if len(L) <= 1: return L, swap_count

    median = len(L) // 2
    left = L[:median]
    right = L[median:]

    left, swap_count = swaps(left, swap_count)
    right, swap_count = swaps(right, swap_count)

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

    #return sorted list and swap count to next level of recursion
    return L, swap_count

# example usage
x = [2, 1, 3, 4]
sorted_x, count = swaps(x)
print(f"Number of swaps: {count}")
print(f"Sorted list: {sorted_x}")