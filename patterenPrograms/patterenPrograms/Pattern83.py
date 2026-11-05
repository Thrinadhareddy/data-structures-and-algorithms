n = int(input("Enter the number of rows:"))
for i in range(n,0,-1):
    print(" "*(i),end="")
    for j in range(n,i-1,-1):
        print(j,end="")
    for k in range(i+1,n+1):
        print(k,end="")
    print()


for i in range(1,n+1):
    print(" "*(i),end="")
    for j in range(n,i,-1):
        print(j,end="")
    for k in range(i+2,n+1):
        print(k,end="")
    print()



 #     5
 #    545
 #   54345
 #  5432345
 # 543212345
 # 5432345
 #  54345
 #   545
 #    5
