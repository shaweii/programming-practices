print("Welcome")
def  triangle(n):
    x = ""
    for i in range(1,n+1):
        for j in range(1,i+1):
            x = x + "*"
        x = x + "\n"
    return x

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
def diamond(n):
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
        
def diamond_reverse(n):
    y = ""
    for i in range(n-1,0,-1):
        for j in range(1,(n-i)+1):
            y = y + "  "
        for k in range(0,2*i-1):
            y = y + "* "
        for j in range(1,(n-i)+1):
            y = y + " "
        y = y + "\n"
    return diamond(a) + y


for m in range(1,10):
   print("1. Triangle")
   print("2. Flipped Triangle")
   print("3. Equilateral triangle")
   print("4. Diamond")
   print("---------------------------------")
   num = int(input("Please choose an option 0-4: "))
   if num == 0:
      print("Goodbye \n")
      continue   
   a = int(input("Enter a number: "))
   if num == 1:
      print("Triangle")
      print(triangle(a))
   elif num == 2:
      print("Flipped Triangle")
      print(flipped_triangle(a))
   elif num == 3:
      print("Equilateral triangle")
      print(equilateral_traingle(a))
   elif num == 4:
      print("Diamond")
      print(diamond_reverse(a))  


    





    
    


