n = int(input("Enter the number of rows:"))
for i in range(n,-1,-1):
    print(" "*(i),end=" ")
    for j in range(i+1,n+1):
        print(chr(64+j),end=" ")
    print()
for i in range(1,n+1):
    print(" "*(i),end=" ")
    for j in range(i+1,n+1):
        print(chr(64+j),end=" ")
    print()




 #     E 
 #    D E
 #   C D E
 #  B C D E
 # A B C D E
 #  B C D E
 #   C D E
 #    D E
 #     E
