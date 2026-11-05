n = int(input("Enter the number of rows:"))
# temp = 0
# for i in range(1,n+1):
#     print(" "*(n-i)*2,(chr(64+i+temp)+" ")*(2*i-1))
#     temp = temp + 1


for i in range(1,n+1):
    print(" "*(n-i)*2,(chr(64+(2*i-1))+" ")*(2*i-1))



# Enter the number of rows:5
#          A
#        C C C
#      E E E E E
#    G G G G G G G
#  I I I I I I I I I
