n = int(input("Please Enter A Number:"))
for i in range(1, n+1):
    for j in range(1,n+1):
        if(j == i+1):
            print(' ', end=' ')
        else:
            print('*', end=' ')
    print()
"""
*   * * * 
* *   * * 
* * *   * 
* * * *   
* * * * * 
"""
-----------------------------------------------
n = int(input("Please Enter A Number:"))
for i in range(1, n+1):
    for j in range(1,i+5):
        if(j+1<=i):
            print(' ', end=' ')
        else:
            print('*', end=' ')
    print()
