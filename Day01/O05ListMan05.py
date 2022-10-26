
"""
1. sort - sorts the original list
2. sorted - takes a copy of the list and then sorts it and returns it
"""

l1 = [10, 5, 8, 6, 9, 3, 1, 4, 7, 2]
print(f"l1 :{l1}")

asc_res = sorted(l1)
print(f"Ascending :{asc_res}")

desc_res = sorted(l1, reverse=True)
print(f"Descending :{desc_res}")

print("=" * 40)
l1 = [10, 'zebra', 'apple', 5, 'yellow', 'blue', 8, 'violet', 'green', 6, 'white', 'pink', 9, 'maroon', 'orange', 3, 'dog', 'sparrow', 1, 'crow', 'red', 4, 'hen', 'nest', 7, 2, 19, 164, 1234, 25, 231, 2045]

print(f"l1 :{l1}")

print("=" * 40)
asc_res = sorted(l1, key=ascii)
print(f"Ascending :{asc_res}")

print("=" * 40)
desc_res = sorted(l1, key=ascii, reverse=True)
print(f"Descending :{desc_res}")

print("=" * 40)
cities = ['thiruvananthapuram', 'hyderabad', 'ooty', 'bangalore', 'chennai', 'delhi', 'vishakapatnam', 'pune', 'mumbai', 'kanyakumari', 'mysore', 'kolkata']

print(f"cities :{cities}")

print("=" * 40)
asc_res = sorted(cities, key=len)
print(f"Ascending :{asc_res}")
desc_res = sorted(cities, key=len)
print(f"Descending :{desc_res}")

