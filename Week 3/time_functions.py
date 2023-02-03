import functions
import time


def time_f(func, n, trials = 10):
    """This runs the function with a value of n 10 times and prints the time for the given variable n"""
    totaltime = 0
    sortTime= []
    #start = time.time()
    for i in range(trials):
        start = time.time()
        func(list(range(n)))
        totaltime += time.time() - start
        sortTime.append(totaltime)
    lowestTime = sorted(sortTime)
    return lowestTime[0]

"""Table for running tests on custom functions, O(1), O(n), O(n^2)"""

print("-"*90) 
print("N",(" "*12), "t_const (ms)",(" "*13), "t_lin (ms)",(" "*18), "t_quad (ms)")
print("-"*90) 

for n in [10, 23, 45, 34, 65, 16, 10, 58, 90]:
    """this for loop will us the list to run all 3 functions through timetrials"""
    x = time_f(functions.func1, n)
    y = time_f(functions.func2, n)
    z = time_f(functions.func3, n)
    print(f"{n:<10}     {x:.20f}     {y:.20f}     {z:.20f}")
print("-"*90) 


"""Python built in atomic behaviors"""
print("-"*90) 
print("N",(" "*12),"t_list (ms)",(" "*14), "t_tup (ms)",(" "*13), "t_str (ms)", (" "*13),"t_set")
print("-"*90) 
for n in (1,2,3,4,5,6,7,8,9,10):
    """this for loop will us the list to run all 3 functions through timetrials"""
    x = time_f(functions.not_in_list, n)
    y = time_f(functions.in_list, n)
    
    print(f"{n:<10}     {x:.20f}     {y:.20f}     ")
    # time_f(functions.func2, n)
    # time_f(functions.func3, n) 
    # print("Function 1: ", end="")
    

    # print("Function 2: ", end="")
    

    # print("Function 3: ", end="")
              

print("-"*90) 