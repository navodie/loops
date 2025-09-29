#finding a number in a list
def finding(list,number):
    for k in list:
        b=1
        if int(k)==int(number):
            print("Yes! the number in the list")
            break
        else:
            b=0
    if b==0:
        print("Sorry! its not there")

finding([5,2,4,7,8,9],1)


    