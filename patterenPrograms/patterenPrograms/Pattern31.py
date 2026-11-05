n = int(input("Enter the number of rows:"))
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(i,end="")
    print()




# Enter the number of rows:5
# 55555
#  4444
#   333
#    22
#     1
