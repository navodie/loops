#  print the multiplication table of any number
def multiplication_for(n):
    m=1
    for i in range(1,11):
        m=n*i
        print(n," * ",i," = ",m)

def multiplication_while(n):
    m=1; j=1
    while j<=10:
        m=n*j
        print(n," * ",j," = ",m)
        j=j+1

n=int(input("Enter n-"))
multiplication_for(n)
multiplication_while(n)

