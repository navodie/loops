def chessboard():
    for i in range(4):
        for i in range(4):
            print("\u2B1c"+"\u2B1b",end="")
        print()
        for i in range(4):
            print("\u2B1b"+"\u2B1c",end="")
        print()

chessboard()

