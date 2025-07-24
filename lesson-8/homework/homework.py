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
