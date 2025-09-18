#right side triangle
def right_triangle_for(rows):
    for i in range(1,rows+1):
        print(" "*(rows-i)+i*"*")

def right_triangle_while(rows):
    m=1
    while m<=rows:
        print(" "*(rows-m)+m*"*")
        m=m+1

rows=int(input("Enter rows-"))
right_triangle_for(rows)
right_triangle_while(rows)