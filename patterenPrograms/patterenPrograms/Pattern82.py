n = int(input("Enter the number of rows:"))
for i in range(n,0,-1):
    print(" "*(i),end="")
    for j in range(i,n+1):
        print(j,end="")
    for k in range(n-1,i-1,-1):
        print(k,end="")
    print()


for i in range(1,n+1):
    print(" "*(i),end="")
    for j in range(i+1,n+1):
        print(j,end="")
    for k in range(n-1,i,-1):
        print(k,end="")
    print()
 # 
 #     5
 #    454
 #   34543
 #  2345432
 # 123454321
 # 2345432
 #  34543
 #   454
 #    5
