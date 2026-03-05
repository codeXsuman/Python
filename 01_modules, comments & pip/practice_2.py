import os

# List contents of the current directory
contents = os.listdir()
print("Directory contents:", contents)

# Or specify a path
path = "/"  # Change this to your desired directory
contents = os.listdir(path)
print(f"Contents of '{path}':", contents)
