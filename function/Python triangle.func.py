print("Python triangle.")
#n = int(input("Please enter a number: "))

def  triangle(n):
    x = ""
    for i in range(1,n+1):
        for j in range(1,i+1):
            x = x + "*"
        x = x + "\n"
    return x

def multi_tringle(a,b):
    t = ""
    for i in range(0,a):
        t = t + triangle(b)
    return t

def incremental_multi_triangle(a):
    t = ""
    for i in range(1,a+1):
        t = t + triangle(i) + a *"-" +"\n"
    return t
    
for l in range(1,100):
    m = int(input("Enter a number or enter 0 to Exit: "))
#g = int(input("Enter a number: "))
#k = triangle(m) + triangle(g)
    if m == 0:
        print("Goodbye")
        break
    k = incremental_multi_triangle(m)
    print(k)
"""f = open("triangle.txt", "w")
f.write(k)"""

#a = triangle(4)
#print(triangle(4))
#print(triangle(8))