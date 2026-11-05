n = int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for k in range(n,1,-1):
    print(" "*(n-k),end=" ")
    for l in range(1,k):
        print("*",end=" ")
    print()


# 
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
