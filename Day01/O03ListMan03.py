
print("Append".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)
l1.append(9)
print(f"l1 :{l1}")

l1.append([10, 11, 12, 13, 14])
print(f"l1 :{l1}")
print(l1[9][1:4])

print("-" * 40)
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")
# extend
l1.extend([7, 8, 9])
l1.extend([10, 11, 12])
print(f"l1 :{l1}")

print("-" * 40)
l1 = [1, 2, 3, 4, 5]
l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)
print(f"l1 :{l1}")

# remove elements from a list
print("pop".center(40, "-"))
l1 = list(range(1, 11))

res = l1.pop(3)
print(f"res :{res}")

res = l1.pop(6)
print(f"res :{res}")

print(f"l1 :{l1}")

res = l1.pop()
print(f"res :{res}")

res = l1.pop()
print(f"res :{res}")

print(f"l1 :{l1}")

print("remove".center(40,"-"))
l2 = [1, 2, 3, 1, 2, 1, 1, 1, 2, 3, 2, 1, 1, 1, 1, 1, 1, 1,2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 3, 1, 1,1 ,1,  1, 1, 1, 1,1, 1,1,1, 1]
print(f"l2 :{l2}")
l2.remove(1)

print(f"l2 :{l2}")
l2.remove(1)
l2.remove(1)
l2.remove(1)
# l2.remove(6)

print("-" * 40)
print(f"l2 :{l2}")
l2 = [1, 2, 3, 1, 2, 1, 1, 1, 2, 3, 2, 1, 1, 1, 1, 1, 1, 1,2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 3, 1, 1,1 ,1,  1, 1, 1, 1,1, 1,1,1, 1]

print("-" * 40)
print(f"l2 :{l2}")
while True:
    try:
        l2.remove(1)
    except ValueError:
        break

print("-" * 40)
print(f"l2 :{l2}")


