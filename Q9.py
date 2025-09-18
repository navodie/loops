#find the sum of all odd number 1 to n
def sum_of_odd_numbers_1ton_for(n):
    sum=0
    for i in range(1,n+1):
        if i%2==0:
            continue
        sum=sum+i
    print("sum using for loop = ",sum)

def sum_of_odd_numbers_1ton_while(n):
    sum1=0; j=1
    while j<=n:
        if j%2==1:
            sum1=sum1+j
        j+=1
    print("sum using while loop = ",sum1)    

n=int(input("Enter n-"))
sum_of_odd_numbers_1ton_for(n)
sum_of_odd_numbers_1ton_while(n)