def  triangle(n):
    x = ""
    num = 65
    for i in range(1,n+1):
        for j in range(1,i+1):
            ch = chr(num)
            x = x + ch
            num = num+1
        x = x + "\n"
            
    return x 
a = int(input("Enter a number: "))
print(triangle(a))