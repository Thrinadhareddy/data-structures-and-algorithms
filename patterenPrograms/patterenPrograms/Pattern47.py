n = int(input("Enter the number of rows:"))
for i in range(n,0,-1):
    print(" "*(i),end="")
    for j in range(n,i-1,-1):
        print(j,end=" ")
    print()




 #     5 
 #    5 4
 #   5 4 3
 #  5 4 3 2
 # 5 4 3 2 1
