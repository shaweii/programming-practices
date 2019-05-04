print("Python flipped triangle.")
n = int(input("Please enter a number: "))
f = open("/Users/sheydaallahweisi/Repos/programming-practices/txt/flipped triangle.txt","w")
for i in range(1,n+1):
    for j in range(n,0,-1):
        if(j <= i):
            f.write("*")
        else:
            f.write(" ")
    f.write("\n")
print("Done")