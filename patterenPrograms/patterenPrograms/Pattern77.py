n = int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print()


#     1
#    2 2
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5
#  4 4 4 4
#   3 3 3
#    2 2
#     1 
