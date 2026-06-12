
def is_palindrome(num):
    temp = num
    reverse = 0

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10

    if reverse == num:
        return True
    else:
        return False

n = int(input("Enter a number: "))

if is_palindrome(n):
    print(n, "is a Palindrome Number")
else:
    print(n, "is not a Palindrome Number")