#check if list is sorted or not
def sorted(n):
    t=False
    if len(n)==1:
        t=True
    else:
        for i in range(0,len(n)-1):
            if n[i]>n[i+1]:
                t=False
            else:
                t=True
    if (t)==True:
        print("Sorted!")
    else:
        print("Not Sorted!")

sorted([1,2,3,4,5,10,6])
        

