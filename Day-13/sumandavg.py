n = int(input("Enter the number of elements: "))

arr = []
total = 0

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
    total = total + num

average = total / n

print("Sum =", total)
print("Average =", average)