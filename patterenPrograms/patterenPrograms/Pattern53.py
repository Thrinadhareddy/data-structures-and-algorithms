n = int(input("Enter the number of rows:"))
for i in range(n,0,-1):
    print(" "*(n-i)*2,end="")
    for j in range(2*i-1):
        print(chr(64+(2*i-1)),end=" ")
    print()

# I I I I I I I I I 
#   G G G G G G G
#     E E E E E
#       C C C
#         A
