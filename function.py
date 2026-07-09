def left_triangle(a):
    left = ""
    for i in range(a):
        left += "  " * (a-i) + "* " * (i+1) + '\n'
    return left[:-1]

a = int(input("enter num: "))
print("--LEFT TRIANGLE--")
print(left_triangle(a))   

def right_triangle(b):
    right = ""
    for i in range(a):
        right += '* ' *(i+1) + '\n'
    return right[:-1]

b = int(input('enter num: '))
print("--RIGHT TRIANGLE--")
print(right_triangle(b))