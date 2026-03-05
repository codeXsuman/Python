# Write a program to find out whether a given post is talking about "Harry" or not.

post = input("Enter your post: ")

if ("harry".lower() in post.lower()): #this will ignore case sensitivity
    print("This post is talking about Harry")

else:
    print("This post is not talking about Harry")