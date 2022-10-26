
print("index".center(40, "-"))

l1 = [1, 2, 3, 1, 1, 1, 1, 1, 2, 3, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3]

print(f"3 :{l1.index(3)}")

print(f"3 :{l1.index(3, l1.index(3) + 1)}")

print(f"3 :{l1.index(3, l1.index(3, l1.index(3) + 1) + 1)}")

print("clear".center(40, "-"))

l1 = list(range(1, 11))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")

print("copy".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 Before :{l1}")
l2 = l1                 # shallow copy (copies both the address and values)
print(f"l2 Before :{l2}")

l2.extend([6, 7, 8, 9])
print(f"l2 After :{l2}")
print(f"l1 After :{l1}")

print("=" * 40)
l3 = [1, 2, 3, 4, 5]
print(f"l3 Before :{l3}")
l4 = l3.copy()                 # deep copy (only values are copied)
print(f"l4 Before :{l4}")

l4.insert(1, 1.5)
l4.insert(3, 2.5)
l4.insert(5, 3.5)
print(f"l4 After :{l4}")
print(f"l3 After :{l3}")

print("=" * 40)
l5 = [1, 2, 3, [10, 20, 30, 40, 50], 4, 5]
print(f"l5 Before :{l5}")
l6 = l5.copy()
print(f"l6 Before :{l6}")

l6[3].extend([60, 70, 80])
print(f"l6 After :{l6}")
print(f"l5 After :{l5}")

print("=" * 40)
l7 = [1, 2, 3, 4, [11, 22, 33, 44, 55], 5]
print(f"l7 Before :{l7}")
from copy import deepcopy
l8 = deepcopy(l7)
print(f"l8 Before :{l8}")

l8[4].append(66)
l8[4].append(77)
print(f"l8 After :{l8}")
print(f"l7 After :{l7}")
