def prime_checker(num):
    if num < 2:
        return f"{num} is neither prime nor composite"
    for i in range(2,num):
        if num % i == 0:
            return f"{num} is composite."
    
    return f"{num} is prime."
        
print(prime_checker(10))
print()