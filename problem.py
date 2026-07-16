# parentheses validation

bracket = '{[(])]}'
stack = []
pairs = {']':'[', ')':'(','}':'{'}

for i in bracket:
    if i in '[{(':
        stack.append(i)
    elif stack and pairs[i] == stack[-1] :
        stack.pop()
    else:
        print(False)
        quit()
print(True)
print(False if stack else True)
    