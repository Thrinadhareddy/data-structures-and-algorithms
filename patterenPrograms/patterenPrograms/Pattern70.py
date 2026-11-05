n = int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(i),end="")
    for j in range(n+1,i,-1):
        print("*",end=" ")
    print()


 # * * * * *
 #  * * * *
 #   * * *
 #    * *
 #     *
