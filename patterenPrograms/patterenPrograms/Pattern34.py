n = int(input("Enter the number of rows:"))
for i in range(n,0,-1):
    print(" "*(n-i),end='')
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print()




# ABCDE
#  ABCD
#   ABC
#    AB
#     A
