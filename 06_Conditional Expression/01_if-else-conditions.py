a = int(input("Enter your age:"))


# if statement one
if(a%2==0):
    print("Even number")

# if statement two
if(a>=18):
    print("you are eligible for vote")

elif(a<0):
    print("Invalid age input")

elif(a==0):
    print("Invalid age input")

else:
    print("you are not eligible for vote")