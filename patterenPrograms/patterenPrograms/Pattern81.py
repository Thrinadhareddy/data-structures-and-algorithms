n = int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
for i in range(1,n+1):
    print(" "*(i),end="")
    for j in range(i+1,n+1):
        print(chr(64+j),end=" ")
    print()




#     A
#    A B
#   A B C
#  A B C D
# A B C D E
#  B C D E
#   C D E
#    D E 
#     E
