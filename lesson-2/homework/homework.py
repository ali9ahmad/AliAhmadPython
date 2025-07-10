1.
current_year = 2025
year_of_birth = int(input("Enter your year of birth: "))
age = current_year - year_of_birth

print(f"Hello, ! You are {age} years old.")

2.
# Sample list of car names
car_names = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'BMW', 'Mercedes', 'Lexus']

# Given text
txt = 'LMaasleitbtui'

# Function to extract car names
def extract_car_names(text, names):
    found_names = []
    for name in names:
        if name in text:
            found_names.append(name)
    return found_names

# Extract car names
extracted_names = extract_car_names(txt, car_names)

# Display the result
print("Extracted car names:", extracted_names)

3.
# Sample list of car names
car_names = ['Mazda', 'Toyota', 'Honda', 'Dodge', 'Nissan', 'BMW', 'Mercedes']

# Given text
txt = 'MsaatmiazD'

# Function to extract car names
def extract_car_names(text, names):
    found_names = []
    text_lower = text.lower()  # Convert to lower case for case-insensitive matching

    for name in names:
        # Check if all characters of the name can be found in the text
        if all(text_lower.count(char) >= name.lower().count(char) for char in set(name.lower())):
            found_names.append(name)

    return found_names

# Extract car names
extracted_names = extract_car_names(txt, car_names)

# Display the result
print("Extracted car names:", extracted_names)

4.
import re

# Given text
txt = "I'am John. I am from London"

# Function to extract residence area
def extract_residence_area(text):
    # Use regex to find the word following "from"
    match = re.search(r'from (\w+)', text)
    if match:
        return match.group(1)
    return None

# Extract residence area
residence_area = extract_residence_area(txt)

# Display the result
print("Residence area:", residence_area)

5.
# Function to reverse a string
def reverse_string(input_string):
    return input_string[::-1]

# Input: user string
user_input = input("Enter a string: ")

# Reverse the string
reversed_string = reverse_string(user_input)

# Display the result
print("Reversed string:", reversed_string)

6.
# Function to count vowels
def count_vowels(input_string):
    vowels = 'aeiouAEIOU'  # Include both lowercase and uppercase vowels
    count = 0
    
    for char in input_string:
        if char in vowels:
            count += 1
            
    return count

# Input: user string
user_input = input("Enter a string: ")

# Count the vowels
vowel_count = count_vowels(user_input)

# Display the result
print("Number of vowels:", vowel_count)

7.
# Function to find the maximum value in a list
def find_maximum(numbers):
    return max(numbers)

# Input: user list of numbers
user_input = input("Enter a list of numbers separated by spaces: ")

# Convert the input string to a list of numbers
number_list = list(map(float, user_input.split()))

# Find the maximum value
maximum_value = find_maximum(number_list)

# Display the result
print("Maximum value:", maximum_value)

8.
# Function to check if a word is a palindrome
def is_palindrome(word):
    # Normalize the word by converting it to lowercase
    normalized_word = word.lower()
    # Check if the word reads the same forward and backward
    return normalized_word == normalized_word[::-1]

# Input: user word
user_input = input("Enter a word: ")

# Check if the word is a palindrome
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")

9.
# Function to extract the domain from an email address
def extract_domain(email):
    try:
        # Split the email at '@' and return the second part
        domain = email.split('@')[1]
        return domain
    except IndexError:
        return None  # Handle case where '@' is not found

# Input: user email address
user_input = input("Enter an email address: ")

# Extract the domain
domain = extract_domain(user_input)

# Display the result
if domain:
    print("Domain:", domain)
else:
    print("Invalid email address.")

10.
import random
import string

# Function to generate a random password
def generate_password(length=12):
    # Define possible characters: letters, digits, and special characters
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits            # 0-9
    special_characters = string.punctuation  # special characters

    # Combine all characters
    all_characters = letters + digits + special_characters

    # Ensure the password contains at least one letter, one digit, and one special character
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 3)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Join the list into a string and return
    return ''.join(password)

# Input: password length
user_input = input("Enter the desired password length (minimum 6): ")
length = max(6, int(user_input))  # Ensure a minimum length of 6

# Generate and display the password
random_password = generate_password(length)
print("Generated password:", random_password)


