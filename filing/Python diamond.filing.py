print("Python diamond.")
n = int(input("Please enter a number: "))
f = open("/Users/sheydaallahweisi/Repos/programming-practices/txt/diamond.txt","w")
for i in range(1, n+1):
    for j in range(1, (n-i)+1):
        f.write("  ")
    for k in range(0,2*i-1):
        f.write("*")
        f.write(" ")
    for j in range(1, (n-i)+1):
        f.write("  ")
    f.write("\n")

for i in range(n-1,0,-1):
    for j in range(1,(n-i)+1):
        f.write("  ")
    for k in range(0,2*i-1):
        f.write("*")
        f.write(" ")
    for j in range(1,(n-i)+1):
        f.write("  ")
    f.write("\n")
print("Done")