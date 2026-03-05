# 2. Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

for i in range(6):
    mark = int(input(f"Enter marks for student {i + 1}: "))
    marks.append(mark)

print("Marks in sorted order:", sorted(marks))  # Displaying the marks in sorted order