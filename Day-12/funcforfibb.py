
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

terms = int(input("Enter the number of terms: "))

print("Fibonacci Series:")
fibonacci(terms)