# Q: 5
# Write a one-line Python expression (no loops) that generates a list of all integers between 1 and 1000 that are:
# divisible by 7 or 9, but not both

# and are palindromic numbers (e.g., 121)

# Submit the GitHub repository link to the code file

abc = []

for i in range(1, 1001):
    if str(i) == str(i)[::-1]:
        if(i % 7 == 0 and i % 9 != 0) or (i % 9 == 0 and i % 7 != 0):
            # print("i: ", i)
            abc.append(i)
            
print(abc) 
        