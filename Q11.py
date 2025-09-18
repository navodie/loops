#count the number of digits in a number
def counting_digits_for(n):
    j=0
    for i in n:
        j=j+1
    print(j)

def counting_digits_while(n):
    j=0
    while j<len(n):
        j=j+1
    print(j)

n=input("Enter n-")
counting_digits_for(n)
counting_digits_while(n)