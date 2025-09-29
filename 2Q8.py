def square(rows):
    print("*"*rows)
    for i in range(rows-1):
        print("*"+" "*(rows-2)+"*")
    print("*"*rows)
square(10)