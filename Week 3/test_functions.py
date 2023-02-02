import functions
import time



def timetrials(func, n, trials = 10):
    """This runs the function with a value of n 10 times and prints the time for the given variable n"""
    totaltime = 0
    #start = time.time()
    for i in range(trials):
        start = time.time()
        func(list(range(n)))
        totaltime += time.time() - start
    print(f"Time taken = {totaltime} for n = {n}")



for n in [10, 23, 45, 34, 65, 16, 107, 508, 9]:
    """this for loop will us the list to run all 3 functions through timetrials"""
    print("Function 1: ", end="")
    timetrials(functions.func1, n)

    print("Function 2: ", end="")
    timetrials(functions.func2, n)

    print("Function 3: ", end="")
    timetrials(functions.func3, n)

    print("-"*100)            