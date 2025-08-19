# 1. Write a python program to display a user entered name followed by Good Afternoon using input () function.

name = input("Enter your name: ")
print("Good Afternoon", name)
# method-2
print(f"Good Afternoon {name}") # this is an f-string for formatting

#==============================================================================
# 2. 
letter = '''Dear {name},
This is a letter to you.
You are invited to the party.
{date}'''
print(letter.replace("{name}", "suman").replace("{date}", "25th December 2050"))

#==============================================================================
# 3 . wirite a programme to detect double space in a string.

name = "harry is a  good  boy."
print(name.find("  ")) # returns the index of the first occurrence of double space
# -1 if not found

#==============================================================================
# 4. replace the double space from problem 3 with single space.
name = "harry  is a good  boy"
print(name.replace("  ", " ")) 
print(name) # this will not change the original string, it will return a new string with double spaces replaced by single space

#==============================================================================
# 5. 
letter = "Dear harry,\n\tThis python cource is nice\nthanks!"
print(letter)



#==================================== END ==========================================
