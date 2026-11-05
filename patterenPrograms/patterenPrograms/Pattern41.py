n = int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i)*2,end='')
    for j in range(1,2*i):
        print(str(chr(64+j))+" ",end="")
    print()




#         A 
#       A B C
#     A B C D E
#   A B C D E F G
# A B C D E F G H I
