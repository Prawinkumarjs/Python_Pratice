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


# # grouping 
# # ex: {john:21, maru:20,alice:21,joe:20}
# # o/p: {20:[joe,maru],21:[john,alice]}

# pupils = {"johnny":21,"sethu":22,"dani":22,"yuvaraj":21}
# team = {}

# for i in pupils:
#     if pupils[i] in team:
#         team[pupils[i]].append(i)
#     else:
#         team[pupils[i]] = [i]

# print(team)

# # largest palindrome in a string

# word = "aaababbcddd"
# res = once = ''
# freq = {}

# for i in word:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i] = 1
# print(freq)
# sortedfreq = sorted(freq,key=lambda x:freq[x])
# print(sortedfreq)

# for i in sortedfreq[::-1]:
#     frequency = freq[i]
#     half = frequency//2
#     if frequency % 2 and not once:
#         res += i*half
#         once = i
#     elif frequency > 1:
#         res += i*half
    
# largestpalindrome = res + once + res[::-1]
# print(largestpalindrome)
# print(largestpalindrome==largestpalindrome)

    
# word pattern: pattern = 'abba', sentence = ' dog cat cat dog'

pattern = 'abba'
sentence = 'dog cat cat dog'
word = sentence.split()
stream = {}

for i in range(len(pattern)):
    currentword, currentmatch = pattern[i],word[i]
    if currentword in stream and stream[currentword]!= currentmatch:
        print(False)
        quit()
    stream[currentword]=currentmatch
print(True)
print(stream)
