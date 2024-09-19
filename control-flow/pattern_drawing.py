size = int(input("Enter the size of the pattern: "))
count = 0
while count < size:
    for item in range(size):
        print("*", end="")
    count +=1
    print()
