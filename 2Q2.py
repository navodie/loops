#print all prime numbers 1 to 100
def prime_numbers_for():
    for i in range(2,101):
        n=1
        for m in range(2,i):
            if i%m==0:
                n=0
                break
        if n==1:
            print(i,sep=" ",end="")
        
        

prime_numbers_for()
                


