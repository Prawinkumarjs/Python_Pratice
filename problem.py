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

# keyboard row

keyBoard = ['qwertyuiop','asdfghjkl','zxcvbnm']
words = ["Hello","Alaska","Dad","Peace",'has','queue','put','gas','ask']
result = []

for i in words:
    word = i.lower()
    row = ""
    for j in word:
        if not row:
            for x in keyBoard:
                if j in x:
                    row  = x
                    break
        elif j not in row:
            break
    else:
        result.append(word)

        
print(result)

    
