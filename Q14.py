#calculate sum of the digits
def getting_sum_for(n):
    m=0
    for i in n:
        m=m+int(i)
    print(m)

def getting_sum_while(n):
    m=0; j=0
    while j<=len(n)-1:
        m=m+int(n[j])
        j=j+1
    print(m)


n=input("Enter n-")
getting_sum_for(n)
getting_sum_while(n)