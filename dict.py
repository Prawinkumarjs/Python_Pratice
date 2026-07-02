# # count frequency

# string = "aaabbbbcccccddddsss"
# fre ={}

# for i in string:
#     if i in fre:
#         fre[i] += 1
#     else:
#         fre[i] = 1
# print(fre)

# sort string wrt frequency

word = "deiii vaaaddaaaa"
freq = {}

for i in word:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1
print(freq)
print(sorted(freq,key=lambda x:freq[x]))
