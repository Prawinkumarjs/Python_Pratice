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

# before chain map

a = {"z": 2, 'y': 3}
c = {"z": 2, 'y': 3}

b = {"z": 1, 'x': 2}
d = {"z": 1, 'y': 1, 'x': 2}
a.update(b)
c.update(d)
print(a)
print(d)

# chain map

default = {'theme': 'light','font':12}
user = {'theme' : 'dark'}
data = ChainMap(default,user)
print(data)


# normal dictionary　doesn't the order concepts

word = OrderedDict([('b' , 2),('c', 1)])
word.setdefault('a',5)
word.move_to_end('b',last=True)
# sen = word
# print(sen)
print(word)
word.popitem(last=True)
# sen.popitem(last=False)
# print(sen)

print(word)
word.popitem(last=True)
# sen.popitem(last=False)

# print(sen)
print(word)



# a = [1,2,3]
# b = [0,5]
# c = b + a

# print(sorted(c))

# deque
data = deque([1,2,3,59,5])
data.rotate(3)
print(data)
data.appendleft(5)
print(data)
data.extendleft([8,9])
print(data)
print(data.pop())
print(data.popleft())
data.extend([10,11])
print(data)

