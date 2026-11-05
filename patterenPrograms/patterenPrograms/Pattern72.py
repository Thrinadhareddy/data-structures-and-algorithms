n = int(input("Enter the number of rows:"))
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()



# 5 4 3 2 1 
#  4 3 2 1
#   3 2 1
#    2 1
#     1
