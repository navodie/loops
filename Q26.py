#more_symbol_triangle
def triangle_for(rows):
    for i in range(1,rows+1):
        if i%2==1:
            print(" "*(rows-i)+(2*i-1)*"*")
        else:
            print(" "*(rows-i)+(2*i-1)*"$")

             

def triangle_while(rows):
    m=1
    while m<=rows:
        if m%2==1:
            print(" "*(rows-m)+(2*m-1)*"*")
        else:
            print(" "*(rows-m)+(2*m-1)*"$")
        m=m+1
triangle_for(5)
triangle_while(5)        