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
1.
def read_file(file_path):
    try:
        with open(file_path, 'r') as file: 
            content = file.read()            
        return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

file_path = 'your_file.txt'  

file_content = read_file(file_path)
print(file_content)

2.
def read_first_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:  
            for _ in range(n):               
                line = file.readline()
                if not line:                 
                    break
                print(line.strip())           
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'your_file.txt' 
n = 5                         

read_first_n_lines(file_path, n)

3.
def append_text_to_file(file_path, text):
    with open(file_path, 'a') as file:  
        file.write(text + '\n')         

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:  
            content = file.read()           
        return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

file_path = 'your_file.txt'  
text_to_append = "This is the text to append."  

append_text_to_file(file_path, text_to_append)

updated_content = read_file(file_path)
print("Updated file content:")
print(updated_content)

4.
def read_last_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:  
            lines = file.readlines()          
            last_n_lines = lines[-n:]        
            for line in last_n_lines:
                print(line.strip())         
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'your_file.txt'
n = 5                      

read_last_n_lines(file_path, n)

5.
def read_file_to_list(file_path):
    lines_list = []  
    try:
        with open(file_path, 'r') as file:
            for line in file:             
                lines_list.append(line.strip())
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return lines_list

file_path = 'your_file.txt'  

lines = read_file_to_list(file_path)

print("Lines in the file:")
for line in lines:
    print(line)

6.
def read_file_to_variable(file_path):
    content = ""  
    try:
        with open(file_path, 'r') as file:  
            for line in file:                
                content += line               
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return content

file_path = 'your_file.txt'  

file_content = read_file_to_variable(file_path)

print("Content of the file:")
print(file_content)

7.
def read_file_to_array(file_path):
    lines_array = []  
    try:
        with open(file_path, 'r') as file:  
            for line in file:               
                lines_array.append(line.strip()) 
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return lines_array

file_path = 'your_file.txt'  

lines = read_file_to_array(file_path)

print("Lines in the file:")
for line in lines:
    print(line)

8.
def find_longest_words(file_path):
    longest_words = []
    max_length = 0
    
    try:
        with open(file_path, 'r') as file:  
            for line in file:                 
                words = line.split()           
                for word in words:             
                    word_length = len(word)     
                    if word_length > max_length:
                        max_length = word_length  
                        longest_words = [word]    
                    elif word_length == max_length:
                        longest_words.append(word)  
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return longest_words

file_path = 'your_file.txt' 

9.
def count_lines_in_file(file_path):
    line_count = 0  
    try:
        with open(file_path, 'r') as file:  
            for line in file:                 
                line_count += 1                
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return line_count

file_path = 'your_file.txt'  

number_of_lines = count_lines_in_file(file_path)

print(f"The number of lines in the file is: {number_of_lines}")

longest_words = find_longest_words(file_path)

print("Longest word(s):")
for word in longest_words:
    print(word)

10.
from collections import Counter
import re

def count_word_frequency(file_path):
    word_count = Counter()  
    
    try:
        with open(file_path, 'r') as file:
            for line in file:             
                
                words = re.findall(r'\b\w+\b', line.lower())
                word_count.update(words) 
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return word_count

file_path = 'your_file.txt'

word_frequencies = count_word_frequency(file_path)

print("Word frequencies:")
for word, count in word_frequencies.items():
    print(f"{word}: {count}")

11.
import os

def get_file_size(file_path):
    try:
        file_size = os.path.getsize(file_path)  
        return file_size
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

file_path = 'your_file.txt' 

size = get_file_size(file_path)

if size is not None:
    print(f"The size of the file is: {size} bytes")

12.
def write_list_to_file(file_path, data_list):
    try:
        with open(file_path, 'w') as file: 
            for item in data_list:            
                file.write(item + '\n')      
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'output.txt'  

data_list = ['Hello, world!', 'This is a test.', 'Writing a list to a file.']

write_list_to_file(file_path, data_list)

print(f"Data has been written to {file_path}.")

13.
def copy_file_contents(source_file_path, destination_file_path):
    try:
        with open(source_file_path, 'r') as source_file:  
            with open(destination_file_path, 'w') as dest_file:  
                for line in source_file:  
                    dest_file.write(line)   
        print(f"Contents copied from {source_file_path} to {destination_file_path}.")
    except FileNotFoundError:
        print("Source file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file_path = 'source.txt'    
destination_file_path = 'destination.txt'  

copy_file_contents(source_file_path, destination_file_path)

14.
def combine_files(file1_path, file2_path, output_file_path):
    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2, open(output_file_path, 'w') as output_file:
            for line1, line2 in zip(file1, file2):  
                combined_line = line1.strip() + ' ' + line2.strip()  
                output_file.write(combined_line + '\n')  
        print(f"Combined lines written to {output_file_path}.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

file1_path = 'file1.txt' 
file2_path = 'file2.txt'
output_file_path = 'combined_output.txt' 

combine_files(file1_path, file2_path, output_file_path)

15.
import random

def read_random_line(file_path):
    try:
        with open(file_path, 'r') as file:  
            lines = file.readlines()         
            if lines:                         
                random_line = random.choice(lines).strip()  
                return random_line
            else:
                return "The file is empty."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

file_path = 'your_file.txt'  

random_line = read_random_line(file_path)


print("Random line from the file:")
print(random_line)

16.
def is_file_closed(file):
    return file.closed


file_path = 'your_file.txt' 

try:
    with open(file_path, 'r') as file: 
     
        print(f"Is the file closed? {is_file_closed(file)}") 
    
    print(f"Is the file closed? {is_file_closed(file)}")  
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")

17.
def remove_newlines_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()  

        modified_content = content.replace('\n', ' ')  

        with open(file_path, 'w') as file:
            file.write(modified_content)

        print(f"Newline characters removed from {file_path}.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'your_file.txt'  

remove_newlines_from_file(file_path)

18.
import re

def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:  #
            content = file.read() 

            words = re.findall(r'\b\w+\b', content) 

            return len(words)  
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

file_path = 'your_file.txt'  

word_count = count_words_in_file(file_path)

if word_count is not None:
    print(f"The number of words in the file is: {word_count}")

19.
def extract_characters_from_files(file_paths):
    characters = []  
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as file:  
                content = file.read()
                characters.extend(list(content)) 
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurred while reading {file_path}: {e}")
    
    return characters

file_paths = ['file1.txt', 'file2.txt', 'file3.txt']  

extracted_characters = extract_characters_from_files(file_paths)

print("Extracted characters:")
print(extracted_characters)

20.
import string

def create_text_files():
    for letter in string.ascii_uppercase:  
        file_name = f"{letter}.txt" 
        with open(file_name, 'w') as file:  
            file.write(f"This is file {file_name}.")  
    print("26 text files created successfully.")

create_text_files()

21.
def create_alphabet_file(file_path, letters_per_line):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  
    lines = []
    
    for i in range(0, len(alphabet), letters_per_line):
        lines.append(alphabet[i:i + letters_per_line])  


    with open(file_path, 'w') as file:
        file.write('\n'.join(lines))  

    print(f"Alphabet written to {file_path} with {letters_per_line} letters per line.")


output_file_path = 'alphabet.txt'  
letters_per_line = 5 


create_alphabet_file(output_file_path, letters_per_line)
