#  # Check whether the anagram or not 
# # method 1
# a = "silent"
# b = "listen"
# if sorted(a) == sorted(b):
#     print("anagram")

# # method 2

# # find the assic value 
# # we can use ord('a')
# # print(ord('a'))

# a = "Kamal"
# a = "kamal"
# b = "malak"

# fl = [0]*26
# sl = [0]*26

# for i in a:
#     fl[ord(i)-97] += 1

# for i in b:
#     sl[ord(i)- 97] += 1

# if fl == sl:
#     print("anagram")
# else:
#     print("not anagram")

# # optimise one

# s1 = "KAMAL"
# s2 = "MAKAL"

# stream1 = [0]*26
# stream2 = [0]*26

# # here s1.lower() is used to lowercase all 

# for i in s1.lower():
#     print(i, ':', ord(i) -97)
#     stream1[ord(i) - 97] += 1

# print("\n")


# for i in s2.lower():
#     print(i, ':', ord(i) -97)
#     stream2[ord(i) - 97] += 1

# print("Anagram" if stream1 == stream2 else "Not Anagram")



# # Compress a String. (Example : aaabbcccc , a3b2c4)


# a = "aaabbbcccz"
# result = ''

# st1 = [0]*26

# for i in a.lower():
#     st1[ord(i) - 97] += 1
#     # print(i, ':', ord(i) -97)
#     # print(st1)  # here is for how the frequency is counted
# # print(st1)  

# index = 0

# for i in st1:
#     if i:
#         print(i)    # for check purpose frequency     
#         result = result + chr(index+97) + str(i) # new result = old result + char(97) + its string contacted frequency
#     index += 1  # this out the if for update and assign

# print(result)


# # First Non Repeating character
# # a = "swiss"
# # here w & i is not repeating but w is first non repeating character

# # method 1 in-built function

# a = 'swiss'
# dup = ""

# for i in a:
#     if a.count(i) == 1:
#         dup = dup + i
#         break
# print(dup)

    

# find the longest word
# eg: Java is te powerful languages, -> language

stream = 'java is powerful language'
print(stream.split())  # used to split the word in btw space

# for i in stream.split():
#     print(i,len(i))     # used to find the length

length = 0
result = ""

for i in stream.split():
    j = len(i)
    if j > length:
        length =  j
        result = i

print(result)
    
