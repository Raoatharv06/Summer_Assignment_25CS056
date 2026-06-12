
def is_armstrong(num):
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** 3
        temp = temp // 10

    if total == num:
        return True
    else:
        return False

n = int(input("Enter a number: "))

if is_armstrong(n):
    print(n, "is an Armstrong Number")
else:
    print(n, "is not an Armstrong Number")