#print all natural numbers n to 1
def print_natural_numbers_nto1_for(n):
    for i in range(n+1):
        print((n+1)-i)

def print_natural_numbers_nto1_while(n):
    m=1
    while m<=n:
        print((n+1)-m)
        m+=1
n=int(input("Enter n-"))
print_natural_numbers_nto1_for(n)
print_natural_numbers_nto1_while(n)