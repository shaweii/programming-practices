print("Python reverse triangle.")
n = int(input("Please enter a number: "))
f = open("/Users/sheydaallahweisi/Repos/programming-practices/txt/reverse triangle.txt","w")
for i in range(n,0,-1):
    for j in range(0,i):
        f.write("*")
    f.write("\n")
print("done")