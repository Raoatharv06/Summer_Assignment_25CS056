
def is_perfect(num):
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total = total + i

    if total == num:
        return True
    else:
        return False

n = int(input("Enter a number: "))

if is_perfect(n):
    print(n, "is a Perfect Number")
else:
    print(n, "is not a Perfect Number")