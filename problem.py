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
    
# reverse a vowel of string

string = "Python is  Program "
vowel = ['a','e','i','o','u']
result = ''
j = 0

# for i in string:
#     if i  in vowel:
#         print(i,end='')

vowels = []

for ch in string:
    if ch in vowel:
        vowels.append(ch)

print(vowels)

vowels.reverse()
print(vowels)

for i in string:
    if i in vowel:
        result = result + vowels[j]
        j = j+1
    else:
        result = result + i

print(string)
print(result)

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