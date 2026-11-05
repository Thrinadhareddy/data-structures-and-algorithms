n = int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i), end="")
    for j in range(i,i+1):
        print(i,end="")
        if i>=2:
            print(" "*(2*i-4),end="")
            for k in range(i,i+1):
                print(i,end="")
    print()


#     1
#    22
#   3  3
#  4    4
# 5      5
