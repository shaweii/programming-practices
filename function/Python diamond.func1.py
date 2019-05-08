print("Python diamond triangle.")
def diamond(n):
    x = ""
    for i in range(1, n+1):
        for j in range(1, (n-i)+1):
            x = x + "  "
        for k in range(0,2*i-1):
            x = x + "* "
        for j in range(1, (n-i)+1):
            x = x + " "
        x = x + "\n"
    return x
        
def diamond_reverse(n):
    y = ""
    for i in range(n-1,0,-1):
        for j in range(1,(n-i)+1):
            y = y + "  "
        for k in range(0,2*i-1):
            y = y + "* "
        for j in range(1,(n-i)+1):
            y = y + " "
        y = y + "\n"
    return diamond(a) + y
a = int(input("Enter a number: "))
print(diamond_reverse(a))

