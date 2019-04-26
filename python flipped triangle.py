print("python flipped triangle.")
n = int(input("Please Enter A Number:"))
for i in range(1,n+1):
    for j in range(n,0,-1):
        if(j < i):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()