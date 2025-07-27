

n = int(input("Enter number of steps : "))  

n1 = 0
n2 = 1
print(n1,end=", ")
print(n2,end=", ") 
for i in range(1, n-1): 
    n3 = n1+n2 
    print(n3,end=", ")
    n1 = n2     
    n2 = n3     
    