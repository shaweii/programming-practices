print("Python vertical multi diamond.")
n = int(input("Please enter a number: "))
m = int(input("Please enter a number for print the number of Vertical rhombuses: "))
f = open("/Users/sheydaallahweisi/Repos/programming-practices/txt/vertical multi diamond.txt" ,"w")
for s in range(1,m+1):
  for i in range(1, n+1):
    for j in range(1, (n-i)+1):
        f.write(" ")
    for k in range(0,2*i-1):
        f.write("*")
    f.write(" ")
    f.write("\n")
  for i in range(n-1,0,-1):
    for j in range(1,(n-i)+1):
        f.write(" ")
    for k in range(0,2*i-1):
        f.write("*")
    f.write(" ")
    f.write("\n")
print("Done")
