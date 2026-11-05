n = int(input("Enter the number of rows:"))
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(i,i+1):
        print(n+1-i,end="")
        if i>=2:
            print(" "*(2*i-4),end="")
            for k in range(i,i+1):
                print(n+1-i,end="")
    print()


#
# 1      1
#  2    2
#   3  3
#    44
#     5
