#largest value in a given number
def largest_one_for(n):
    m=0
    for i in str(n):
        if m<int(i):
            print("Largest one is ", i)
        else:
            print("Largest one is ", m)
        m=int(i)

def largest_one_while(n):
    m=0;k=1;j=0
    while k<=len(n):
        if j<int(n[m]):
            print("Largest one is ", n[m])
        else:
            print("Largest one is ",j)
        j=int(n[k])
        k=k+1

largest_one_for(78568)
largest_one_while(23421)

