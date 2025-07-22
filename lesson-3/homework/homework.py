#1. 
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

third_fruit = fruits[2]
print("The third fruit is:", third_fruit)

#2.
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

combined_list = list1 + list2

print("Concatenated List:", combined_list)

3.
numbers = [10, 20, 30, 40, 50, 60, 70]

first_element = numbers[0]
middle_element = numbers[len(numbers) // 2]
last_element = numbers[-1]

extracted_elements = [first_element, middle_element, last_element]

print("Extracted Elements:", extracted_elements)

4.
favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Shawshank Redemption", "Parasite"]

movies_tuple = tuple(favorite_movies)

print("Favorite Movies Tuple:", movies_tuple)

5.
cities = ["New York", "London", "Paris", "Tokyo", "Berlin"]

if "Paris" in cities:
    print("Paris is in the list.")
else:
    print("Paris is not in the list.")

6.
original_list = [1, 2, 3, 4, 5]

duplicated_list = original_list + original_list

print("Duplicated List:", duplicated_list)

7.
numbers = [10, 20, 30, 40, 50]

if len(numbers) > 1:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]

print("List after swapping first and last elements:", numbers)

8.
numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

slice_tuple = numbers_tuple[3:8]  

print("Sliced Tuple:", slice_tuple)

9.
colors = ["red", "blue", "green", "blue", "yellow", "blue", "purple"]

blue_count = colors.count("blue")

print("The color 'blue' appears", blue_count, "times in the list.")

10.
animals = ("cat", "dog", "lion", "tiger", "elephant")

lion_index = animals.index("lion")

print("The index of 'lion' is:", lion_index)

11.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

merged_tuple = tuple1 + tuple2

print("Merged Tuple:", merged_tuple)

12.
my_list = [1, 2, 3, 4, 5]
my_tuple = (10, 20, 30, 40)

list_length = len(my_list)
tuple_length = len(my_tuple)

print("Length of the list:", list_length)
print("Length of the tuple:", tuple_length)

13.
numbers_tuple = (1, 2, 3, 4, 5)

numbers_list = list(numbers_tuple)

print("Converted List:", numbers_list)

14.
numbers_tuple = (5, 2, 9, 1, 7)

max_value = max(numbers_tuple)
min_value = min(numbers_tuple)

print("Maximum value:", max_value)
print("Minimum value:", min_value)

15.
words_tuple = ("apple", "banana", "cherry", "date")

reversed_tuple = words_tuple[::-1]

print("Reversed Tuple:", reversed_tuple)
