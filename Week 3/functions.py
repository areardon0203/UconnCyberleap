def func1(L):
    """this returns the value of L for a cost of 1"""
    return L

def func2(L):
    """This returns the value of L + I through interation for a cost of n"""
    for i in L:
        return i + 23

def func3(L):
    """This returns a sorted list of L for a cost of n^2"""
    items = []
    for i in L:
        items.append(i)
    return sorted(items)

# def not_in_list(L):
#     """Looks for a number that is not in the given list"""
#     return 50 in L

# def in_list(L):
#     """Looks for a number that is within a given list"""
#     return 5 in L

# def tuple(L):
#     return (3,4) in L