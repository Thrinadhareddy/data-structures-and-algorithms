n = int(input("Enter the number of rows:"))
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(i,0,-1):
        print(chr(64+i),end=" ")
    print()



# E E E E E 
#  D D D D
#   C C C
#    B B
#     A
