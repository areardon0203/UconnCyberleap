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

def bs_sublist(L, item, left= 0, right = None):
    left, right = 0, len(L)
    while right - left > 1:
        median = (right + left) // 2
        if item < L[median]:
            right = median
        else:
            left = median
    return right > left and L[left] == item

def opt_insertion_sort(L): pass

def insertion_sort(L):
    """Naive insertion sort. Adaptive, but still slow."""
    n = len(L)
    for j in range(n): # go through every item
        for i in range(n - 1 - j, n - 1): # bubble it into a sorted sublist
            if L[i] > L[i+1]:                 # 1 comparison
                L[i], L[i+1] = L[i+1], L[i]   # 2 writes 
            else: break

if __name__ == '__main__':
    "Print out a table comparing insertion to opt_insertion"
    import timeit, random
    random.seed = 652

    def print_table(title, L, ns):
        'helper function for printing a nice table w/ timeit'

        # header
        width = 38
        print(title.center(width, "="))
        print(f"{'n':<8}{'insert (ms)':<15}{'opt insert (ms)':<15}")
        print("-"*width)

        # body
        for n in ns:
            print(f"{n:<8}", end = '')
            print(f"{1000*timeit.timeit(f'insertion_sort(L[:{n}])', number=1, globals=globals()):<15.0f}", end = '')
            print(f"{1000*timeit.timeit(f'opt_insertion_sort(L[:{n}])', number=1, globals=globals()):<15.0f}")
        
        # footer
        print("-"*width)

    ns = [1000, 2000, 3000, 4000, 5000]
    L = [random.randint(0,ns[-1]) for i in range(ns[-1])]
    print_table("Random Distribution", L, ns)

    # L = [5, 1, 4, 2, 8, 0, 2]
    # cocktail_sort(L)
    # print("Sorted array is:")
    # for i in range(len(L)):
    #     print ("%d"  % L[i])