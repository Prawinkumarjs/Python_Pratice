# # parentheses validation

# bracket = '{[(])]}'
# stack = []
# pairs = {']':'[', ')':'(','}':'{'}

# for i in bracket:
#     if i in '[{(':
#         stack.append(i)
#     elif stack and pairs[i] == stack[-1] :
#         stack.pop()
#     else:
#         print(False)
#         quit()
# print(True)
# print(False if stack else True)
    
# # reverse a vowel of string

# string = "Python is  Program "
# vowel = ['a','e','i','o','u']
# result = ''
# j = 0

# # for i in string:
# #     if i  in vowel:
# #         print(i,end='')

# vowels = []

# for ch in string:
#     if ch in vowel:
#         vowels.append(ch)

# print(vowels)

# vowels.reverse()
# print(vowels)

# for i in string:
#     if i in vowel:
#         result = result + vowels[j]
#         j = j+1
#     else:
#         result = result + i

# print(string)
# print(result)

# # clear and gpt version
# string = "Python is Program"
# vowel = ['a','e','i','o','u']
# result = ''
# j = 0

# vowels = []

# # Collect vowels
# for ch in string:
#     if ch in vowel:
#         vowels.append(ch)

# print(vowels)

# # Reverse vowels
# vowels.reverse()
# print(vowels)

# # Replace vowels
# for i in string:
#     if i in vowel:
#         result = result + vowels[j]
#         j = j + 1
#     else:
#         result = result + i

# print(result)
# # daniel's version

# string = "Python Is A Programming Language"
# string = list(string)
# index1 = 0
# index2 = len(string)-1
# while index1<=index2:
#     first = string[index1] in 'AEIOUaeiou'
#     second = string[index2] in 'AEIOUaeiou'
#     if first and second:
#         string[index1],string[index2] = string[index2],string[index1];index1+=1;index2-=1
#     if not first:
#         index1 += 1
#     elif not second:
#         index2 -= 1
# print(''.join(string))

# # keyboard row

# keyBoard = ['qwertyuiop','asdfghjkl','zxcvbnm']
# words = ["Hello","Alaska","Dad","Peace",'has','queue','put','gas','ask']
# result = []

# for i in words:
#     word = i.lower()
#     row = ""
#     for j in word:
#         if not row:
#             for x in keyBoard:
#                 if j in x:
#                     row  = x
#                     break
#         elif j not in row:
#             break
#     else:
#         result.append(word)

        
# print(result)

    
# form words in diagonal flow

# words = ['car','can','lid']
# c a r
# c a n
# l i d
# o/p = ['c','ca','ral','in','d']

word = ['car','can','lid']



# equal score strings
# dbb = 8 ; d = 4 == 4 = bb(2)
# abcd = 10 ; ab = 3 != 7 = cd(3,4) 

strings = 'dbbe'
stream = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

right = left = 0

for i in strings:
    right += stream[i]
    

for j in strings:
    value = stream[j]
    left += value
    right -= value

    if left == right:
        print(True)
        break

else:
    print(False)


# method 2
strings = 'dbb'
j=[]
for i in strings:
    j.append((ord(i)-ord("a"))+1)
l=[]
for k in j:
    l.append(j[0])
    j.pop(0)
    if(sum(j)==sum(l)):
        print("True")
        break
else:
    print("False")