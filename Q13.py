#swap first and last digits
def swap_digits(n):
    print(n[-1]+n[1:len(n)-1:1]+n[0])

n=input("Enter n-")
swap_digits(n)