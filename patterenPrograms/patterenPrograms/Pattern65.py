n = int(input("Enter the number of rows:"))
for i in range(n,0,-1):
    for j in range(i,n+1):
        print(chr(64+j),end=" ")
    print()
for k in range(2,n+1):
    for l in range(k,n+1):
        print(chr(64+l),end=" ")
    print()




# E
# D E
# C D E
# B C D E
# A B C D E
# B C D E
# C D E 
# D E
# E
