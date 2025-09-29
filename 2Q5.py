def grid(rows):
    for j in range(rows):
        for i in range(1,rows+1):
            print(i,sep="  ",end="")
        print()


grid(4)
