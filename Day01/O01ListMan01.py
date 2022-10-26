
l1 = list()
print(f"l1 {l1}")               # interpolation
print(type(l1))                 # RTTI - Runtime type identification
print("-" * 40)
l2 = [1, 2, 3, 4, 5, 'six', 'seven', 'eight', True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
# memory allocation is not contigious
print("addresses of the list elements")
l1 = [1, 2, 3, 4, 5, 'six', 'seven', 'eight', True, False]
print(f"{l1[1]} :{id(l1[1])}")
print(f"{l1[2]} :{id(l1[2])}")
print(f"{l1[3]} :{id(l1[3])}")
print(f"{l1[5]} :{id(l1[5])}")


# add elements into the list
print("-" * 40)
l1 =  [1, 2, 3, 4, 5]
print(f"l1 :{l1}")
l1[3] = 33
print(f"l1 :{l1}")

# read elements from the list
print("-" * 40)
l2 = list(range(1, 11))
print(f"l2 :{l2}")
for i in l2:
    print(i, end=" ")
print()
print(f"l1[0] :{l1[0]}")
print(f"l1[1] :{l1[1]}")

print("-" * 40)
print(f"l2 :{l2}")
l2[3] = 33
l2[7] = 77
print(f"l2 :{l2}")

print("-" * 40)
# delete elements of a list
print(f"l2 :{l2}")
del l2[3]
del l2[6]

print(f"l2 :{l2}")

print("-" * 40)
l1 = [1, 2, 3]
print(f"l1 :{l1}")
a, b, c = l1
print(a, b, c, sep= " : ")

print("-" * 40)
l2 = list(range(1,11))
print(f"l2 :{l2}")

*a, b, c = l2
print(a, b, c, sep=" : ")

a, *b, c = l2
print(a, b, c, sep=" : ")

a, b, *c = l2
print(a, b, c, sep=" : ")

print("-" * 40)
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [l1, l2]
print(f"l3 :{l3}")
print(len(l3))

print("-" * 40)
l4  = [*l1, *l2]                # unpack
print(f"l4 :{l4}")
print(len(l4))
