# write a programme using functions to find greatest of three numbers.

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    if(b>a and b>c):
        return b
    if(c>b and c>a):
        return c
    
a = 1
b = 2
c = 3
print(f"Greatest number is: {greatest(a, b, c)}")