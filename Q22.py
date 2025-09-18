#rhombus
def rhombus_for(n):
    for i in range(1,n+1):
        print(" "*(n-i)+"*"*n)

def rhombus_while(n):
    print()
    m=1
    while m<=n:
        print(" "*(n-m)+"*"*n)
        m=m+1

n=int(input("Enter n-"))
rhombus_for(n)
rhombus_while(n)