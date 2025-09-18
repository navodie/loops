#print all natural numbers from 1 to n
def print_all_natural_numbers_for(n):
    for i in range(n+1):
        print(i)
def print_all_natural_numbers_while(n):
    m=1
    while m<=n:
        print(m)
        m+=1
        
n=int(input("Enter n-"))
print_all_natural_numbers_for(n)
print_all_natural_numbers_while(n)
