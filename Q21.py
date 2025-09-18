#rectangle
def rectangle_for(h,w):
    for i in range(h):
        print(w*"*")

def rectangle_while(h,w):
    print()
    m=1
    while m<=h:
        print(w*"*")
        m=m+1

h=int(input("Enter h-"))
w=int(input("Enter w-"))
rectangle_for(h,w)
rectangle_while(h,w)