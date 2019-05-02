print("Python horizontal multi diamond.")
n = int(input("Please enter a number:"))
y = int(input("Please enter a number for print the number of horizontalrhombuses:"))
for i in range(1, n+1):
    for x in range(1,y+1):
        for j in range(1, (n-i)+1):
            print(end="  ")
        for k in range(0,2*i-1):
            print("* ", end="")
        for j in range(1, (n-i)+1):
            print(end="  ")
    print()

for i in range(n-1,0,-1):
    for x in range(1,y+1):
        for j in range(1,(n-i)+1):
            print(end="  ")
        for k in range(0,2*i-1):
            print("* ", end="")
        for j in range(1,(n-i)+1):
            print(end="  ")
    print()


