1.
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return f"The result is: {result}"

number1 = 10
number2 = 0  

print(divide_numbers(number1, number2))

2.
def get_integer_input():
    user_input = input("Please enter an integer: ")
    try:
        number = int(user_input)
        return number
    except ValueError:
        raise ValueError("Error: Input is not a valid integer.")

try:
    result = get_integer_input()
    print(f"You entered the integer: {result}")
except ValueError as e:
    print(e)

3.
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."

filename = input("Please enter the filename to open: ")
result = read_file(filename)
print(result)

4.
def get_numbers():
    try:
        num1 = input("Please enter the first number: ")
        num2 = input("Please enter the second number: ")
        
        num1 = float(num1)
        num2 = float(num2)
        
        return num1, num2
    except ValueError:
        raise TypeError("Error: Both inputs must be numerical values.")
try:
    number1, number2 = get_numbers()
    print(f"You entered: {number1} and {number2}")
except TypeError as e:
    print(e)

5.
def open_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except PermissionError:
        return f"Error: You do not have permission to access the file '{filename}'."
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."

filename = input("Please enter the filename to open: ")
result = open_file(filename)
print(result)

6.
def access_list_element(my_list, index):
    try:
        element = my_list[index]
        return f"The element at index {index} is: {element}"
    except IndexError:
        return f"Error: Index {index} is out of range for the list."

sample_list = [10, 20, 30, 40, 50]

try:
    user_index = int(input("Please enter an index to access: "))
    result = access_list_element(sample_list, user_index)
    print(result)
except ValueError:
    print("Error: Please enter a valid integer for the index.")

7.
def get_user_input():
    try:
        user_input = input("Please enter a number: ")
        number = float(user_input)
        return number
    except KeyboardInterrupt:
        print("\nInput was cancelled. Exiting the program.")
        exit()
    except ValueError:
        print("Error: Please enter a valid number.")

number = get_user_input()
print(f"You entered: {number}")

8.
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return f"The result of {num1} divided by {num2} is: {result}"
    except ArithmeticError:
        return "Error: An arithmetic error occurred. Please check your inputs."

try:
    numerator = float(input("Please enter the numerator: "))
    denominator = float(input("Please enter the denominator: "))
    result = divide_numbers(numerator, denominator)
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")

9.
def open_file_with_encoding(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except UnicodeDecodeError:
        return f"Error: There was an encoding issue while reading the file '{filename}'."
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."

filename = input("Please enter the filename to open: ")
result = open_file_with_encoding(filename)
print(result)

10.
def perform_list_operation(my_list):
    try:

        result = my_list.non_existent_method()
        return result
    except AttributeError:
        return "Error: The list does not have the specified attribute or method."

sample_list = [1, 2, 3, 4, 5]
result = perform_list_operation(sample_list)
print(result)

# Python File Input Output: Exercises, Practice, Solution

