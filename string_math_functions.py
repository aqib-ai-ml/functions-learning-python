# String and Maths Functions

def reverse(str1):
    return str1[::-1]

print(reverse("Myself"))
print()


def palindrome(str1):
    if str1 == str1[::-1]:
        return f"{str1} is a palindrome."
    else:
        return f"{str1} is not a palindrome."

print(palindrome("malayalam"))
print(palindrome("Nurse"))
print()


def vowel(str1):
    vowels = ['a', 'e', 'i', 'o', 'u']
    str1 = str1.lower()

    dic = {}

    for i in str1:
        if i in vowels:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

    return dic

print(vowel("alphabet"))
print()


def factorial(n):
    m = 1
    for i in range(1, n + 1):
        m *= i
    return m

print(factorial(5))
print()


def prime_checker(num):
    if num < 2:
        return f"{num} is neither prime nor composite"

    for i in range(2, num):
        if num % i == 0:
            return f"{num} is composite."

    return f"{num} is prime."

print(prime_checker(10))
print()


def fibonacci(num):
    a = 0
    b = 1
    lst = []

    for i in range(num):
        lst.append(a)
        a, b = b, a + b

    return lst

print(fibonacci(7))
print()


def fibonacci_recursive(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)

print(fibonacci_recursive(8))