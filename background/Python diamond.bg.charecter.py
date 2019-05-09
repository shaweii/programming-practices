print("Python diamond triangle.")
def diamond(n,bc,fc):
    x = ""
    for i in range(1, n+1):
        for j in range(1, (n-i)+1):
            x = x + bc + " "
        for k in range(0,2*i-1):
            x = x + fc + " " 
        for j in range(1, (n-i)+1):
            x = x + bc + " "
        x = x + "\n"
    return x       
def diamond_reverse(n,bc,fc):
    y = ""
    for i in range(n-1,0,-1):
        for j in range(1,(n-i)+1):
            y = y + bc + " "
        for k in range(0,2*i-1):
            y = y + fc + " " 
        for j in range(1,(n-i)+1):
            y = y + bc + " "
        y = y + "\n"
    return diamond(a,bc,fc) + y
bc = input("Please enter a charecter for background: ")
fc = input("Please enter a charecter for diamond style: ")
a = int(input("Enter a number: "))
print(diamond_reverse(a,bc,fc))

