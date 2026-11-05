n = int(input("Enter the number of rows:"))
for i in range(n,0,-1):
    print(" "*(n-i)*2,end="")
    for j in range(2*i-1):
        print(chr(65+j),end=" ")
    print()



# A B C D E F G H I
#   A B C D E F G
#     A B C D E
#       A B C
#         A 
