n = int(input("Enter the number of rows:"))
for i in range(n,-1,-1):
    print(" "*(i),end="")
    for j in range(n,i-1,-1):
        print(j,end=" ")
    print()
for k in range(0,n+1):
    print(" "*(k),end=" ")
    for l in range (n,k,-1):
        print(l,end=" ")
    print()




#     4 
#    4 3
#   4 3 2
#  4 3 2 1
# 4 3 2 1 0
#  4 3 2 1
#   4 3 2
#    4 3
#     4
#
