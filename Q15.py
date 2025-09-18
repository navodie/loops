#calculate product of the digits
def getting_product_for(n):
    m=1
    for i in n:
        m=m*int(i)
    print(m)

def getting_product_while(n):
    m=1; j=0
    while j<=len(n)-1:
        m=m*int(n[j])
        j=j+1
    print(m)


n=input("Enter n-")
getting_product_for(n)
getting_product_while(n)