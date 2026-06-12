reverse = 0

def reverse_number(n):
    global reverse

    if n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        reverse_number(n // 10)

num = int(input("Enter a number: "))

reverse_number(num)

print("Reversed number =", reverse)