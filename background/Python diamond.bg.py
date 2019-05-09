print("Python diamond triangle.")
num = ""
n = ""
print("1. @")
print("2. #")
print("3. $")
print("4. %")
print("5. &")
print("6. *")
number = int(input("Please choose an option 1-6 for background: "))
print("---------------------------------")
if number == 1:
    num = 64
elif number == 2:
    num = 35
elif number == 3:
    num = 36
elif number == 4:
    num =37
elif number == 5:
    num = 38
elif number == 6:
    num = 42
def diamond(n):
    x = ""
    for i in range(1, n+1):
        for j in range(1, (n-i)+1):
            ch = chr(num)
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
            ch = chr(num)
            y = y + ch + " "
        for k in range(0,2*i-1):
            y = y + "- " 
        for j in range(1,(n-i)+1):
            y = y + ch + " "
        y = y + "\n"
    return diamond(a) + y
a = int(input("Enter a number: "))
print(diamond_reverse(a))

