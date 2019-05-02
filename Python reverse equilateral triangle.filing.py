print("Python equilateral triangle.")
n = int(input("Please enter a number: "))
f = open("equilateral triangle.txt" ,"w")
for i in range(n-1,0,-1):
    for j in range(1,(n-i)+1):
        f.write(" ")
    for k in range(0,2*i-1):
        f.write("*")
    f.write("\n")
    for j in range(1,(n-i)+1):
        f.write(" ")
    f.write("\n")
print("Done")
    

