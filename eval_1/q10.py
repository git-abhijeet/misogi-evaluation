students = [
    {"name": "Alice", "marks": [80, 75, 90]},
    {"name": "Bob", "marks": [70, 60, 65]},
    {"name": "Charlie", "marks": [95, 85, 100]},
    {"name": "David", "marks": [60, 70, 80]}
]

A = []
B = []
C = []
result = {}

for i in students:
    # print(i["marks"])
    s = 0
    avg = 0
    for j in i['marks']:
        # print(i, j)
        s += j
    # print(s)
    avg = int(s/3)
    # print(avg)
    
    if avg >= 85:
        print("name: A", i["name"])
        A.append(i['name'])
    elif avg >= 70:
        print("name: B", i["name"])
        B.append(i['name'])
    else:
        print("name: C", i["name"])
        C.append(i['name'])

result["A"] = A
result["B"] = B
result["C"] = C

print("result: ", result)