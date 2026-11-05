n = int(input("Enter the number of rows:"))
for i in range(n,0,-1):
    for j in range(i,n+1):
        print(chr(64+i),end=" ")
    print()
for k in range(2,n+1):
    for l in range(k,n+1):
        print(chr(64+k),end=" ")
    print()

# E
# D D
# C C C
# B B B B
# A A A A A
# B B B B 
# C C C
# D D
# E
