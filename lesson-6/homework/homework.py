1.
def modify_string_with_underscores(txt):
    result = []
    count = 0
    
    for i, char in enumerate(txt):
        result.append(char)
        count += 1
        
        if count == 3 and char.lower() not in 'aeiou' and (i + 1 < len(txt) and txt[i + 1] != '_'):
            result.append('_')
            count = 0
        elif char == '_':
            count = 0

    return ''.join(result)

print(modify_string_with_underscores("hello"))                
print(modify_string_with_underscores("assalom"))              
print(modify_string_with_underscores("abcabcabcdeabcdefabcdefg"))

2.
n = int(input("Enter an integer: "))

for i in range(n):
    print(i ** 2)

3.
def print_natural_numbers():
    i = 1
    while i <= 10:
        print(i)
        i += 1

print_natural_numbers()

4.
def print_multiplication_table(number):
    i = 1
    while i <= 10:
        print(number * i)
        i += 1

num = int(input("Enter a number: "))
print_multiplication_table(num)

5.
numbers = [12, 75, 150, 180, 145, 525, 50]

for number in numbers:
    if number > 50:
        print(number)

6.
def count_digits(number):
    return len(str(number))

num = int(input("Enter a number: "))
digit_count = count_digits(num)
print("Output:", digit_count)

7.
def print_reverse_number_pattern(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()  

num = 5
print_reverse_number_pattern(num)

8.
list1 = [10, 20, 30, 40, 50]

for i in range(len(list1) - 1, -1, -1):
    print(list1[i])

9.
for number in range(-10, 0):
    print(number)

10.
for number in range(5):
    print(number)
print("Done!")

11.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = 25
end = 50

print(f"Prime numbers between {start} and {end}:")
for number in range(start, end + 1):
    if is_prime(number):
        print(number)

12.
# Function to display Fibonacci series
def fibonacci_series(n):
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(n):
        print(a, end='  ')
        a, b = b, a + b

terms = 10
fibonacci_series(terms)

13.

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

number = 5
result = factorial(number)
print(f"{number}! = {result}")

14.
def uncommon_elements(list1, list2):
    from collections import Counter
    
    count1 = Counter(list1)
    count2 = Counter(list2)
    
    uncommon = []
    
    for element in count1:
        if element not in count2:
            uncommon.extend([element] * count1[element])
    
    for element in count2:
        if element not in count1:
            uncommon.extend([element] * count2[element])
    
    return uncommon

print(uncommon_elements([1, 1, 2], [2, 3, 4]))  
print(uncommon_elements([1, 2, 3], [4, 5, 6]))  
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5])) 
