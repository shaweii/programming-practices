print("Python diamond triangle.")
num = int(input("Please enter a number for background(0-126): "))
for num in range(0,126):
    ch = chr(num)
def diamond(n):
    x = ""
    for i in range(1, n+1):
        for j in range(1, (n-i)+1):
            x = x + ch + " "
        for k in range(0,2*i-1):
            x = x + "- " 
        for j in range(1, (n-i)+1):
            x = x + ch + " "
        x = x + "\n"
    return x       
def diamond_reverse(n):
    y = ""
    for i in range(n-1,0,-1):
        for j in range(1,(n-i)+1):
            y = y + ch + " "
        for k in range(0,2*i-1):
            y = y + "- " 
        for j in range(1,(n-i)+1):
            y = y + ch + " "
        y = y + "\n"
    return diamond(a) + y
a = int(input("Enter a number: "))
print(diamond_reverse(a))

