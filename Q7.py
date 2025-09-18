#find the sum of all natural numbers 1 to n
def sum_of_n_for(n):
    sum=0
    for i in range(n+1):
        sum=sum+i
    print(sum)

def sum_of_n_while(n):
    sum1=0; j=1
    while j<=n:
        sum1=sum1+j
        j+=1
    print(sum1)

n=int(input("Enter n-"))
sum_of_n_for(n)
sum_of_n_while(n)

