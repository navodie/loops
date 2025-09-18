#find the sum of all even number 1 to n
def sum_of_even_numbers_1ton_for(n):
    sum=0
    for i in range(1,n+1):
        if i%2==1:
            continue
        sum=sum+i
    print("sum = ",sum)

def sum_of_even_numbers_1ton_while(n):
    sum1=0; j=1
    while j<=n:
        if j%2==0:
            sum1=sum1+j
        j+=1
    print("sum with using while = ",sum1)    

n=int(input("Enter n-"))
sum_of_even_numbers_1ton_for(n)
sum_of_even_numbers_1ton_while(n)
