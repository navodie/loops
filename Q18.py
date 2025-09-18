#checking palindrome or not
def palindrome_ornot(n):
    print(n)
    m=n[-1::-1]
    print(m)
    if m==n:
        print("yess!")
    else:
        print("noo!")

n=input("Enter n-")
palindrome_ornot(n)