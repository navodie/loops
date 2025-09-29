def multiplication(rows):
    for i in range(1,rows+1):
        for j in range(1,rows+1):
            print(i*j,sep="  ",end="")
        print()
multiplication(4)
