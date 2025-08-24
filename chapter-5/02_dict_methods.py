marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    0: "harry"
}

print (marks.items())
print (marks.keys())
print (marks.values())
marks.update({"Alice" : 90, "harry" : 77})
print(marks)

print(marks.get("Alice2")) # print none
print(marks["Alice2"]) # raises KeyError



