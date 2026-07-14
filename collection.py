from collections import *

vord = 'aabbccddeeffgg'
print(Counter(vord))

data = defaultdict(int)
for i in vord:
    data[i] += 1

print(data)

data1 = defaultdict(list)
for i in vord:
    data1[i] += [1]

print(data1)
