n = int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end='')
    for j in range(1,i+1):
        print(i-j,end="")
    for k in range(1,i):
        print(k,end="")
    print()



#     0
#    101
#   21012
#  3210123
# 432101234
