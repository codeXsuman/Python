s = set()

s.add(20)
s.add(20.0)
s.add('20')

print(s)  # it will print only two values because 20 and 20.0 are considered same value in set.

print(len(s))  # 2

