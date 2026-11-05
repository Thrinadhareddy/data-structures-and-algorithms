n = int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i)*2,end='')
    for j in range(2*i-1,0,-1):
        print(str(chr(64+j))+" ",end="")
    print()




#         A 
#       C B A
#     E D C B A
#   G F E D C B A
# I H G F E D C B A
