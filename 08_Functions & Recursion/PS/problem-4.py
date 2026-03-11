# write a recursive function to calculate sum of first n natural numbers.

def sum(n):
    if(n==1): # base case to prevent going in minus values
        return 1
    s = n + sum(n-1)
    return s

n = int(input("Enter a number: "))
print(f"sum of first {n} numbers = {sum(n)}")