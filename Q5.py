#print all even numbers between 1 to n
def all_even_numbers_for(n):
    for i in range(1,n+1):
        if i%2==1:
            continue
        print(i)

def all_even_numbers_while(n):
    j=1
    while j<=n:
        if j%2==0:
            print(j)
        j+=1

n=int(input("Enter n-"))
all_even_numbers_for(n)
all_even_numbers_while(n)
    
