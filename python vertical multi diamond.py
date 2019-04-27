print("python vertical multi diamond.")
n = int(input("Please Enter A Number:"))
m = int(input("Please Enter A Number for To print the number of rhombuses:"))
k = 0
s = 1
for s in range(1,m+1):
  for i in range(1, n+1):
    for j in range(1, (n-i)+1):
        print(end="  ")
    while k != (2*i-1):
        print("* ", end="")
        k = k + 1
    k = 0
    print()
  for i in range(n-1,0,-1):
    for j in range(1,(n-i)+1):
        print(end="  ")
    while k != (2*i-1):
        print("* ", end="")
        k = k + 1
    k = 0
   
    print()
