# WAP to calculate the factorial of a given number using for loop.

n = int(input("Enter the number: "))

product = 1

for i in range(1,n+1): # goes 1 to n
    product = product * i 

print(f"factorial of {n} is {product}")