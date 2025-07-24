1.
def is_leap(year):
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

2.
def evaluate_number(n):
    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0:  
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")

n = int(input("Enter an integer: "))
evaluate_number(n)

3.
def find_even_numbers_if_else(a, b):
    if a > b:
        a, b = b, a  # Swap if a is greater than b

    evens = []
    if a % 2 == 0:
        evens.append(a)
        a += 2
    else:
        a += 1

    while a <= b:
        evens.append(a)
        a += 2

    return evens

a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))
print("Even numbers:", find_even_numbers_if_else(a, b))
