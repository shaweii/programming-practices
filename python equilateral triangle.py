print("python equilateral triangle.")
n = int(input("Please Enter A Number:"))
k = 0

for i in range(1, n+1):
    for space in range(1, (n-i)+1):
        print(end="  ")
    while k != (2*i-1):
        print("* ", end="")
        k = k + 1
    k = 0
    print()
