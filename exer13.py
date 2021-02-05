rows = int(input("Input number of rows: "))

for row in range(1,rows+1):
    for space in range (rows+1,row,-1):
        print(" ", end="")
    for column in range (1, row+1 ):
        print(str(row)+" ", end="")
    print()





