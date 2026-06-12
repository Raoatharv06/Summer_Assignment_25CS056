def find_max(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

maximum = find_max(num1, num2)

print("Maximum number =", maximum)
