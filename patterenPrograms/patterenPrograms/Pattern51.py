n = int(input("Enter the number of rows:"))
for i in range(n,0,-1):
    print(" "*(n-i)*2,end="")
    for j in range(2*i-1):
        print(j+1,end=" ")
    print()




# 1 2 3 4 5 6 7 8 9 
#   1 2 3 4 5 6 7
#     1 2 3 4 5
#       1 2 3
#         1
