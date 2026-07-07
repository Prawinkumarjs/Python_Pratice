a = {1,2,3,5}
b = {2,4,6,7}

result1 = a.union(b)
result2 = a.difference(b)
result3 = a.intersection(b)
a1 = a.copy()
print(result1)
print(result2)
print(result3)
print(a1)

a1.add(8)
print(a1)

a1.update([22,23,25])
print(a1)

a1.difference_update(a)
print(a1)
c = {1,2,3,5}
c1 = {1, 2, 3, 5, 8, 22, 23, 25}
c1.intersection_update(c)
print(c1)
print(c)
c.pop()
print(c)
print(b)
b.discard(4)
print(b)