# star pattern

n = int(input("Enter no of lines: "))

for i in range(1,n+1):
    print(" "* (n-i), end="")
    print("*" * (2*i-1), end="") # STAR FORMULA= (2*i-1)
    print("")

