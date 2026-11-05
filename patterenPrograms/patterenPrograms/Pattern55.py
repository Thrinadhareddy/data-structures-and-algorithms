from itertools import chain
n = int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for k in range(n,1,-1):
    print(" "*(n-k),end=" ")
    for l in range(1,k):
        print(l,end=" ")
    print()


# for i in chain(range(1,n+1),range(n-1,0,-1)):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# Enter the number of rows:5
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5
#  1 2 3 4
#   1 2 3
#    1 2
#     1
