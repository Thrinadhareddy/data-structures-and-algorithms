n = int(input("Enter the number of rows:"))
for i in range(n,-1,-1):
    for j in range(n,i,-1):
        print(chr(64+j),end=" ")
    print()
for k in range(1,n+1):
    for l in range(n,k,-1):
        print(chr(64+l),end=" ")
    print()





# E
# E D
# E D C
# E D C B 
# E D C B A
# E D C B
# E D C
# E D
# E
