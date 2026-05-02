def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    elif operation == "**":
        return a**b
    else:
        return "Invalid operation"
print("\n--- Calculator ---")
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print()
op = input("Enter operation (+, -, *, /, **): ")

print()

result =  calculator(x, y, op)
print("Result:", result)
