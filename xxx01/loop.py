for a in ["cat", "dog", "parrot"]:
    print(a)

sum = 0
for p in [10, 14, 16, 3]:
    sum += p
print(sum)

for x in range(4):
    for y in range(3):
        print(f"{x, y}")

numbers = [5, 2, 5, 2, 2]
for x in numbers:
    xx = "x" * x
    print(f"{xx}")

numbers = [5, 2, 5, 2, 2]
for x in numbers:
    output = ""
    for y in range(x):
        output += "x"
    print(output)

numbers = [52, 25, 54, 29, 25]
numbers.insert(3, 85)
max = numbers[0]
for n in numbers:
    if max < n:
        max = n
print(max)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for n in row:
        print(n)

numbers = [52, 25, 54, 29, 25, 25, 54, 33]
uniges = []
for n in numbers:
    if n not in uniges:
        uniges.append(n)
print(uniges)

private_endpoints = {
    "blob": "10.100.4.5",
    "table": "10.100.4.6"
}
for p, ip in private_endpoints.items():
    print(p)
    print(ip)
