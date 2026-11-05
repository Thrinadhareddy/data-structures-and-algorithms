n = int(input("Enter the number of rows:"))
for i in range(n,-1,-1):
    print(" "*(i),end=" ")
    for j in range(i,n+1):
        print(j,end=" ")
    print()
for k in range(1,n+1):
    print(" "*(k),end=" ")
    for l in range(k,n+1):
        print(l,end=" ")
    print()


 # 
 #    3
 #   2 3
 #  1 2 3
 # 0 1 2 3
 #  1 2 3
 #   2 3
 #    3
