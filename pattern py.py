# BUTTER FLY AND PRINT X IN ONE CODE
for x in range (20):
    for y in range(20):
        if   y==0 or y==19:
            print("*",end=" ")
        elif y==x:
            print("*",end=" ")
        elif y==19-x:
            print("*",end=" ")


        else:
            print(" ",end=" ")

    print()