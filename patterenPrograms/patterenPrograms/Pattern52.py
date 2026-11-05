n = int(input("Enter the number of rows:"))
for i in range(n,0,-1):
    print(" "*(n-i)*2,end="")
    for j in range(2*i-1):
        print(chr(64+i),end=" ")
    print()




# E E E E E E E E E 
#   D D D D D D D
#     C C C C C
#       B B B
#         A
