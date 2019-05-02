print("Python triangle.")
n = int(input("Please enter a number: "))
f = open("triangle" ,"w")
for i in range(1,n+1):
    for j in range(1,i+1):
        f.write("*")
    f.write("\n")
print("Done")  

     
  




"""i = 1
while i <= n:
    print("*"*i)
    i += 1
f = open("demofile.txt", "a")
"""


