# Write a program which finds out whether a given name is present in a list or not.

names = ['harry', 'ron', 'hermione', 'draco', 'luna']

name = input("Enter your name: ")

if name in names:
    print("Your name is present in the list")

else:
    print("Your name is not present in the list")