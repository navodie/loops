#output the first and last number 
def output(n):
    print(n[0], n[-1])

def output_for(n):
    j=0
    for i in n:
        j=j+1
    print(n[0],n[j-1])

def output_while(n):
    j=0; m=1
    while m<=len(n):
        j=j+1
        m=m+1
    print(n[0],n[j-1])




n=input("Enter n-")
output(n)
output_for(n)
output_while(n)