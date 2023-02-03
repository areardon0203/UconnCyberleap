import functions
import time


def time_f(func, n, trials = 10):
    """This runs the function with a value of n 10 times and prints the time for the given variable n"""
    totaltime = 0
    #start = time.time()
    for i in range(trials):
        start = time.time()
        func(list(range(n)))
        totaltime += time.time() - start
    print(n, "  ",totaltime)

print("-"*90) 
print("N    ", "t_const (ms)              ", "t_lin (ms)              ", "t_quad (ms)")
for n in [10, 23, 45, 34, 65, 16, 10, 58, 90]:
    """this for loop will us the list to run all 3 functions through timetrials"""
    time_f(functions.func1, n)  
    time_f(functions.func2, n)
    time_f(functions.func3, n) 
    # print("Function 1: ", end="")
    

    # print("Function 2: ", end="")
    

    # print("Function 3: ", end="")
              

print("-"*90) 
