
def rem(l, word):
    n = []
    for items in l:
        if not(items == word):
            n.append(items.strip(word))
    return n

l = ["harry", "Rohan", "Subham", "an"]

print(rem(l, "an"))