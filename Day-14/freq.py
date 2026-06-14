n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

key = int(input("Enter the element to find frequency: "))

count = 0

for i in arr:
    if i == key:
        count += 1

print("Frequency of", key, "=", count)