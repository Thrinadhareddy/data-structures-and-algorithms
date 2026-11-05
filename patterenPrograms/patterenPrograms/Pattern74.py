n = int(input("Enter the number of rows:"))
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(i,0,-1):
        print(chr(64+j),end=" ")
    print()


#
# E D C B A
#  D C B A
#   C B A
#    B A
#     A 
