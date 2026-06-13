n = int(input("Enter the number of elements: "))

arr = []
even_count = 0
odd_count = 0

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

for i in arr:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even elements =", even_count)
print("Number of odd elements =", odd_count)