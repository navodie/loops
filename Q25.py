#spaced triangle
def spaced_triangle_for(rows):
    for i in range(1,rows+1):
        print(" "*(rows-i)+(i)*"* ")

def spaced_triangle_while(rows):
    m=1
    while m<=rows:
        print(" "*(rows-m)+(m)*"* ")
        m=m+1

spaced_triangle_for(5)
spaced_triangle_while(5)