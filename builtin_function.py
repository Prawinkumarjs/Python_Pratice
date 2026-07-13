list1 = [1,2,3,4]

print([x for x in list1 if x%2==0])

print(list(filter(lambda x : x%2==0,list1)))   # here lambda act as for loop just as eg only

print([x for x in list1 if x%2])

print(list(filter(lambda x : x%2,list1)))

print([x **2 for x in list1 if x%2])

print(list(map(lambda x : x**2, list1)))

twodlist = [[1,2,3],[4,5,6],[7,8,9]]
twoDlist = [[1,2],[4, 6],[ 8,9]]
twolist = [[1,2],[4 ],[ 8,9]]

print(list(zip(*twodlist)))
print(list(zip(*twoDlist)))
print(list(zip(*twolist)))

print(any([x%2==0 for x in [2,4,5]]))
print(any([x%2==0 for x in [2,4,6]]))

print(all([x%2==0 for x in [2,4,5]]))
print(all([x%2==0 for x in [2,4,6]]))
