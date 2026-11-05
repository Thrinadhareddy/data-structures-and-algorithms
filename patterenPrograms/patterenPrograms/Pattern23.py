n = int(input("Enter the number of rows:"))
for i in range(0,n):
    for j in range(n,i,-1):
        print(chr(64+j),end=' ')
    print()




#
# Enter the number of rows:10
# J I H G F E D C B A
# J I H G F E D C B
# J I H G F E D C
# J I H G F E D
# J I H G F E
# J I H G F
# J I H G
# J I H
# J I
# J
