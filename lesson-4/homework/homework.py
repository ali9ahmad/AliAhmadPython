1.
my_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}

sorted_ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))

sorted_descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Sorted in Ascending Order:", sorted_ascending)
print("Sorted in Descending Order:", sorted_descending)

2.
my_dict = {0: 10, 1: 20}

my_dict[2] = 30

print("Updated Dictionary:", my_dict)

3.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

combined_dict = {**dic1, **dic2, **dic3}

print("Combined Dictionary:", combined_dict)

4.
n = 5

squared_dict = {}

for x in range(1, n + 1):
    squared_dict[x] = x * x

print("Generated Dictionary:", squared_dict)

5.
squared_dict = {}

for x in range(1, 16):
    squared_dict[x] = x * x

print("Generated Dictionary:", squared_dict)


# Set Exercises
1.
my_set = {1, 2, 3, 4, 5}

print("Created Set:", my_set)

2.
my_set = {1, 2, 3, 4, 5}

print("Iterating over the set:")
for item in my_set:
    print(item)

3.
my_set = {1, 2, 3}

print("Original Set:", my_set)

my_set.add(4)
print("After adding 4:", my_set)

my_set.update([5, 6, 7])
print("After adding 5, 6, and 7:", my_set)

4.
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

my_set.remove(3)
print("After removing 3:", my_set)

my_set.discard(2)
print("After discarding 2:", my_set)

my_set.clear()
print("After clearing the set:", my_set)

5.
my_set = {1, 2, 3, 4, 5}

print("Original Set:", my_set)

item_to_remove = 3

if item_to_remove in my_set:
    my_set.remove(item_to_remove)
    print(f"Removed {item_to_remove}: {my_set}")
else:
    print(f"{item_to_remove} not found in the set.")













