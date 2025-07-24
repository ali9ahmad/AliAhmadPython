1.
def is_prime(n):
    if n <= 1:
        return False 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False 
    return True  

print(is_prime(4))  
print(is_prime(7))  

2.
def digit_sum(k):
    total = 0
    for digit in str(k):  
        total += int(digit) 
    return total

print(digit_sum(24))   
print(digit_sum(502))  

3.
def powers_of_two(N):
    k = 0
    result = []
    while True:
        power = 2 ** k
        if power > N:
            break
        result.append(power)
        k += 1
    return result

N = 10
print("Natija:", ' '.join(map(str, powers_of_two(N)))) 

