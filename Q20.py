#upper side triangle
def upper_side_triangle_for(rows):
    for i in range(rows):
        print((rows-i)*"*")

def upper_side_triangle_while(rows):
    m=0
    while m<rows:
        print((rows-m)*"*")
        m=m+1

rows=int(input("enter rows-"))
upper_side_triangle_for(rows)
upper_side_triangle_while(rows)