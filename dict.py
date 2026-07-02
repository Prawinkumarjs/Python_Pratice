# # count frequency

# string = "aaabbbbcccccddddsss"
# fre ={}

# for i in string:
#     if i in fre:
#         fre[i] += 1
#     else:
#         fre[i] = 1
# print(fre)

# # sort string wrt frequency

# word = "deiii vaaaddaaaa"
# freq = {}

# for i in word:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i] = 1
# print(freq)
# print(sorted(freq,key=lambda x:freq[x]))


# grouping 
# ex: {john:21, maru:20,alice:21,joe:20}
# o/p: {20:[joe,maru],21:[john,alice]}

pupils = {"johnny":21,"sethu":22,"dani":22,"yuvaraj":21}
team = {}

for i in pupils:
    if pupils[i] in team:
        team[pupils[i]].append(i)
    else:
        team[pupils[i]] = [i]

print(team)
