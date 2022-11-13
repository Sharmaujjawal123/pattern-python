for x in range (10):
    for y in range(10):
        if   y==0 or y==9:
            print("*",end=" ")
        elif y<=x:
            print("*",end=" ")
        elif y<=9-x:
             print("*",end=" ")


        else:
            print(" ",end=" ")

    print()