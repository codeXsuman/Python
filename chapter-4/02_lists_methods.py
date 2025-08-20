friends = ["apple", "orange", 345.9, 5, True, "Akash", "Ravi"]
print(friends)

friends.append("Mango")  # Adding an element to the end of the list
print(friends)

Aa = [1,34,7,8,3,23,11,5]

Aa.sort()  # Sorting the list in ascending order
print(Aa)

Aa.reverse()  # Reversing the order of the list
print(Aa)


Aa = (1,34,7,8,3,23,11,5)
Aa.insert(2, 9999)  # Inserting an element at index 2
print(Aa)

print(Aa.pop(1))  # pop = Removing and returning the 2nd element (34)
print(Aa)


print(type(Aa))