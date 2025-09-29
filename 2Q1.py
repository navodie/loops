#if a number is prime or not
def prime_or_not(n):
    T=0; 
    if n==1:
         print("True")
    elif n==2:
         print("True")         
    elif n==3:
         print("True")
    else:
        for m in range(2,n):
            if n%m==0:
                t=0
            else:
                t=1
            k=(t==1)or(T==1)
            if t==0:
                break
        print(k)
        m=m+1
        T=t
n=int(input("Enter n-"))
prime_or_not(n)
        