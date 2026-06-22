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



# Compress a String. (Example : aaabbcccc , a3b2c4)


a = "aaabbbcccz"
result = ''

st1 = [0]*26

for i in a.lower():
    st1[ord(i) - 97] += 1
    # print(i, ':', ord(i) -97)





    

