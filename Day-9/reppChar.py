rows = int(input("Enter number of rows: "))

for i in range(rows):
    ch = chr(65 + i)

    for j in range(i + 1):
        print(ch, end="")

    print()