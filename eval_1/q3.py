# Q: 3
# Write two programs that sum squares of numbers from 1 to 10 million:
# Using normal loop

# Using multithreading

# Measure time taken by each using time module.

# Discuss whether the threading approach actually helps in Python and why or why not (GIL concept).

# Submit the GitHub repository link to the code file

import time

start = time.time()

def sum_square(n):
    total = 0
    
    for i in range(1, n+1):
        total = total + i*i
        
    print("total: ", total)
    # print(start)
    # print(time.time())
    print("time: ", time.time() - start)
    

sum_square(100000000)