print("Python equilateral triangle.")
def equilateral_traingle(n):
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
a = int(input("Enter a number: "))
print(equilateral_traingle(a))