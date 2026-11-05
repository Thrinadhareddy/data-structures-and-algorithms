n = int(input("Enter the number of rows:"))
# temp = 0
# for i in range(1,n+1):
#     print(" "*(n-i)*2,end="")
#     for j in range(1,i+temp+1):
#         print("* ",end="")
#     temp = temp + 1
#     print()

# for i in range(1, n+1):
#     print(" " * (n-i) * 2, end="")
#     for j in range(2*i - 1):       # ← replaces i + temp
#         print("* ", end="")
#     print()


for i in range(1,n+1):
    print(" "*(n-i)*2,"* "*(2*i -1),end="")
    print()




# Enter the number of rows:5
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
