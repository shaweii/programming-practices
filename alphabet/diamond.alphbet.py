print("Python diamond triangle.")
def diamond(n):
    x = ""
    num = 65
    for i in range(1, n+1):
        for j in range(1, (n-i)+1):
            x = x + "  "
        for k in range(0,2*i-1):
            ch = chr(num)
            x = x + ch + " "
            num = num+1
            if num == 91:
                num = 65      
        for j in range(1, (n-i)+1):
            x = x + " "
        x = x + "\n"
    return x       
def diamond_reverse(n):
    y = ""
    num = 90
    ch = chr(num)
    for i in range(n-1,0,-1):
        for j in range(1,(n-i)+1):
            y = y + "  "
        for k in range(0,2*i-1):
            ch = chr(num)
            y = y + ch + " "
            num = num - 1
            if num == 64:
                num =90
        for j in range(1,(n-i)+1):
            y = y + " "
        y = y + "\n"
    return diamond(a) + y
a = int(input("Enter a number: "))
print(diamond_reverse(a))

