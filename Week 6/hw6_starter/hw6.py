# TODO: implement the following 3 functions. Use docstrings, whitespace, and comments.

def cocktail_sort(L, swapped = True, start = 0, end = None): 
    n = len(L) # find length of L
    if end == None: end = n-1

    while swapped:
        swapped = False

        for i in range(start, end):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                swapped = True

        if not swapped:
            break

        swapped = False

        end -= 1
    
        for i in range(end-1, start-1, -1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                swapped = True

        start += 1

def bs_sublist(L, left, right, item):
    while right - left > 0:
        median = (left + right) // 2
        if item > L[median]:
            left = median + 1
        else:
            right = median
    return left 

    
def opt_insertion_sort(L):
    for i in range(1, len(L)):
        item = L[i]
        pos = bs_sublist(L, 0, i, item)
        for j in range(i, pos, -1):
            L[j] = L[j - 1]
        L[pos] = item

def insertion_sort(L):
    """Naive insertion sort. Adaptive, but still slow."""
    n = len(L)
    for j in range(n): # go through every item
        for i in range(n - 1 - j, n - 1): # bubble it into a sorted sublist
            if L[i] > L[i+1]:                 # 1 comparison
                L[i], L[i+1] = L[i+1], L[i]   # 2 writes 
            else: break

if __name__ == '__main__':
    # "Print out a table comparing insertion to opt_insertion"
    # import timeit, random
    # random.seed = 100

    # def print_table(title, L, ns):
    #     'helper function for printing a nice table w/ timeit'

    #     # header
    #     width = 38
    #     print(title.center(width, "="))
    #     print(f"{'n':<8}{'insert (ms)':<15}{'opt insert (ms)':<15}")
    #     print("-"*width)

    #     # body
    #     for n in ns:
    #         print(f"{n:<8}", end = '')
    #         print(f"{1000*timeit.timeit(f'insertion_sort(L[:{n}])', number=1, globals=globals()):<15.0f}", end = '')
    #         print(f"{1000*timeit.timeit(f'opt_insertion_sort(L[:{n}])', number=1, globals=globals()):<15.0f}")
        
    #     # footer
    #     print("-"*width)

    # ns = [1000, 2000, 3000, 4000, 5000]
    # L = [random.randint(0,ns[-1]) for i in range(ns[-1])]
    # print_table("Random Distribution", L, ns)

    L = [5, 1, 4, 2, 8, 0, 2]
    print(L)
    opt_insertion_sort(L)
    print("Sorted array is:")
    for i in range(len(L)):
        print ("%d"  % L[i], end="")