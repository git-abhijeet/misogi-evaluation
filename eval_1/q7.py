# Q: 7
# Write a generator prime_generator(n) that yields the first n prime numbers efficiently.

# Write a decorator measure_time that prints how long it takes to generate those primes.

# Submit the GitHub repository link to the code file

import time

def measure_time(func):
    def abc(n):
        s = time.time()
        a = func(n)
        e = time.time()
        print("Time: ", s, "-",  e)
        return a
    return abc 



@measure_time
def prime_generator(n):
    n = 2
    c = []
    
    while(len(c) < n):
        prime = True
        # for i in range(2)
        