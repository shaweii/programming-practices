print("Python triangle.")
n = int(input("Please enter a number: "))
f = open("/Users/sheydaallahweisi/Repos/programming-practices/txt/triangle.txt" ,"w")
for i in range(1,n+1):
    for j in range(1,i+1):
        f.write("*")
    f.write("\n")
print("Done")  


