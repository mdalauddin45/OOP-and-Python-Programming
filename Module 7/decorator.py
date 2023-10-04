import math
import time
def timer(func):
    def inner(*args,**kwargs):
        print('time stated')
        start = time.time()
        func(*args,**kwargs)
        print('time ended')
        end = time.time()
        print(f'total time taken {end-start}')
    return inner

# timer()()

@timer
def get_factorial(n):
    print('Factorial Starting')
    result = math.factorial(n)
    print(f'factorial {n} is : {result}')
    
get_factorial(n=5)

# timer(get_factorial())