#left side triangle
def left_triangle_for(rows):
    for i in range(1,rows+1):
        print(i*"*")

def left_triangle_while(rows):
    m=1
    while m<=rows:
        print(m*"*")
        m=m+1

rows=int(input("Enter rows-"))
left_triangle_for(rows)
left_triangle_while(rows)

