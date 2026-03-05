# star pattern 3

n = int(input("Enter no of lines: "))

for i in range(1,n+1):
    if(i==1 or i == n): # first or last row --> print all stars
        print("*" * n, end="")
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*", end="")
        # this upper three lines will print '*' 'space' '*' till i == n
    print("") # will sattle every line in next line