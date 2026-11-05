n = int(input("Enter the number of rows:"))
for i in range(n,-1,-1):
    for j in range(n,i-1,-1):
        print(j,end=" ")
    print()
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(j,end=" ")
    print()



#
# 4
# 4 3
# 4 3 2
# 4 3 2 1
# 4 3 2 1 0
# 4 3 2 1
# 4 3 2
# 4 3
# 4
