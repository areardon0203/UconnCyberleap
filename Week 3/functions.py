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
