print("Python vertical multi diamond.")
n = int(input("Please enter a number: "))
m = int(input("Please enter a number for print the number of Vertical rhombuses: "))
for s in range(1,m+1):
  for i in range(1, n+1):
    for j in range(1, (n-i)+1):
        print(end="  ")
    for k in range(0,2*i-1):
        print("* ", end="")
    print()
  for i in range(n-1,0,-1):
    for j in range(1,(n-i)+1):
        print(end="  ")
    for k in range(0,2*i-1):
        print("* ", end="")
    print()
"""
another code for this style.
print("Python vertical multi diamond.")
n = int(input("Please enter a number: "))
m = int(input("Please enter a number for print the number of Vertical rhombuses: "))
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
    """