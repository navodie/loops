#output the factorial value of n
def fac_n_for(n):
    f=1
    for i in range(1,n+1):
        f=f*int(i)
    print(f)

def fac_n_while(n):
    f=1; m=1
    while m<=n:
        f=f*m
        m=m+1
    print(f)


n=int(input("Enter n-"))
fac_n_for(n)
fac_n_while(n)

