print("Python flipped triangle.")
#n = int(input("Please enter a number: "))
def flipped_triangle(n):
    x =""
    for i in range(1,n+1):
        for j in range(n,0,-1):
            if(j <= i):
               x = x + "* "
            else:
               x = x + "  "
        x = x + "\n"
    return x
a = int(input("Enter a number: "))
print(flipped_triangle(a))
