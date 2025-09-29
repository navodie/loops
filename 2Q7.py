def shapes(rows):
    for i in range(1,rows+1):
        print(" "*(rows-i),end="")
        for j in range(1,i+1):
            print(str(j),end="")
        for k in range(i-1,0,-1):
            print(str(k),end="")
        print()
shapes(10)


