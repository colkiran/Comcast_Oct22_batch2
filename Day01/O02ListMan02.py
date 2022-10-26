
l1 = ['a', 'b', 'c', 'd', 'e', 'f']
print(f"l1 :{l1}")

print("-" * 40)
for l in l1:
    print(l, end=" ")
print()

print("-" * 40)
for l in enumerate(l1):
    print(l, end= " ")
print()

print("-" * 40)
for l in enumerate(l1):
    print(l[0], l[1])

print("-" * 40)
for index, letter in enumerate(l1):
    print(index, letter)

print("-" * 40)
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"mylist :{mylist}")

for lst in mylist:
    print(lst)
print("-" * 40)

for ind, lst in enumerate(mylist):
    print(f"{ind}\t{lst}")

print("-" * 40)
for ind, lst in enumerate(mylist):
    print(f"list({ind})")
    for idx, num in enumerate(lst):
        print(f"\t{idx}\t{num}")
print("-" * 40)

for lst in mylist:
    for num in lst:
        print(num, end=" ")
    print()

