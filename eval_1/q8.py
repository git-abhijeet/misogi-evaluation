# Q: 8
# Create a file sales.json which contains:

# [
#   {"id": 1, "item": "Pen", "price": 20, "qty": 5},
#   {"id": 2, "item": "Notebook", "price": 100, "qty": 2},
#   {"id": 3, "item": "Bag", "price": 500, "qty": 1}
# ]
# Read this file, compute total revenue per item, and write results into report.txt as formatted strings:
# Pen → ₹100
# Notebook → ₹200
# Bag → ₹500
# Implement it safely using context managers and handle file errors gracefully.
# Submit the GitHub repository link to the code file

import json

with open("sales.json", "r") as abc:
    a = json.load(abc)
    
    print(a)
    
    r = {}
    
    for i in a:
        r[i["item"]] = i["price"] * i["qty"]
        
    print("r:  ", r)