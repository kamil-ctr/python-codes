'''
Print the pattern
*****
****
***
**
*
'''

n = int(input("Number of rows : "))
for i in range(0, n):   
    for j in range(0, n-i):  
        print("Hi",end="")
    print("")