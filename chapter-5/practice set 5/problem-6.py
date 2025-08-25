# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

favorite_languages = {}

name = input("Enter friends name:")
language = input("Enter favorite language:")
favorite_languages.update({name: language})

name = input("Enter friends name:")
language = input("Enter favorite language:")
favorite_languages.update({name: language})

name = input("Enter friends name:")
language = input("Enter favorite language:")
favorite_languages.update({name: language})

name = input("Enter friends name:")
language = input("Enter favorite language:")
favorite_languages.update({name: language})

print(favorite_languages)
