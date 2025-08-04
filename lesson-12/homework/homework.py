#1.

import threading
import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, prime_list):
    """Worker function to find prime numbers in a given range."""
    for num in range(start, end):
        if is_prime(num):
            prime_list.append(num)

def main(start, end, num_threads):
    """Main function to manage threads and check for prime numbers."""
    threads = []
    prime_list = []
    thread_range = (end - start) // num_threads

    for i in range(num_threads):
        thread_start = start + i * thread_range
        thread_end = start + (i + 1) * thread_range if i < num_threads - 1 else end
        
        thread = threading.Thread(target=check_primes, args=(thread_start, thread_end, prime_list))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print(f"Prime numbers in range {start} to {end}: {sorted(prime_list)}")

if __name__ == "__main__":
    start_range = 1
    end_range = 100
    num_threads = 4  # Change this value for more or fewer threads

    main(start_range, end_range, num_threads)

#2.
import threading
from collections import defaultdict

def count_words(file_chunk, word_count):
    """Worker function to count words in a given chunk of text."""
    local_count = defaultdict(int)
    
    for line in file_chunk:
        words = line.split()
        for word in words:
            local_count[word] += 1

    # Update the shared word count dictionary
    with threading.Lock():
        for word, count in local_count.items():
            word_count[word] += count

def main(file_path, num_threads):
    """Main function to manage threads and word counting."""
    word_count = defaultdict(int)
    threads = []

    # Read the file and divide it into chunks
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    chunk_size = len(lines) // num_threads

    for i in range(num_threads):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size if i < num_threads - 1 else len(lines)
        file_chunk = lines[start_index:end_index]

        thread = threading.Thread(target=count_words, args=(file_chunk, word_count))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("Word occurrences:")
    for word, count in sorted(word_count.items()):
        print(f"{word}: {count}")

if __name__ == "__main__":
    file_path = 'large_text_file.txt'  # Specify your file path here
    num_threads = 4  # Change this value for more or fewer threads

    main(file_path, num_threads)
