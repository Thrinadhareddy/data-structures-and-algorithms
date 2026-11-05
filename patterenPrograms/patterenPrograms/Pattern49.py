n = int(input("Enter the number of rows:"))
for i in range(n,0,-1):
    print(" "*(n-i)*2,end="")
    for j in range(2*i-1):
        print(i,end=" ")
    print()



# 5 5 5 5 5 5 5 5 5
#   4 4 4 4 4 4 4
#     3 3 3 3 3
#       2 2 2
#         1
