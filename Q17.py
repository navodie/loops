#fibonacci series
def fibonacci_for(n):
    f1=0; f2=1
    if n==1:
        print(f1)
    elif n==2:
        print(f2)
    else:
        for i in range(3,n+1):
            f=f1+f2
            f1=f2; f2=f
        print(f)

def fibonacci_while(n):
    b1=0; b2=1; m=3
    if n==1:
        print(b1)
    elif n==2:
        print(b2)
    else:
        while m<=n:
            b=b1+b2
            b1=b2; b2=b
            m=m+1
        print(b)

n=int(input("enter n-"))
fibonacci_for(n)
fibonacci_while(n)
    

