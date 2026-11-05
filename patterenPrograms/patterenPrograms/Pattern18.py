n = int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(n+1,i,-1):
        print(chr(64+i),end=' ')
    print()



# Enter the number of rows:10
# A A A A A A A A A A
# B B B B B B B B B
# C C C C C C C C
# D D D D D D D
# E E E E E E
# F F F F F
# G G G G
# H H H
# I I
# J
