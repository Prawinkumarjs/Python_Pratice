# square
def square():
    a = int(input('Enter num: '))
    for i in range(a):
        print("* " * a)

# hollow square
def hollowsquare():
    a = int(input('Enter num: '))
    for i in range(a):
        if i == 0 or i == a-1:
            print("* " * a)
        else:
            print("* " + "  " * (a-2) + "* ")

# left triangle
def lefttriangle():
    a = int(input('Enter num: '))
    for i in range(a+1):
        print("* " * i)

# hollow left triangle
def hollowlefttriangle():
    a = int(input('Enter num: '))
    for i in range(1,a+1):
        if i == 1 or i == a:
            print("* " * i)
        else:
            print("* " + "  " * (i - 2) + "* ")

# right triangle
def righttriangle():
    a = int(input('Enter num: '))
    for i in range(a):
        print("  " * (a-i-1) + "* " * (i+1))

# hollow right triangle 
def hollowrighttriangle():
    a = int(input("Enter num: "))
    for i in range(a):
        if i == 0 or i == a-1:
            print("  " * (a-i-1) + "* " * (i+1))
        else:
            print("  " * (a-i-1) + "* " + "  " *(i-1) + "* ")

# left inverted triangle
def leftinvertedtriangle():
    a = int(input("Enter num: "))
    for i in range(a):
        # print("* " * (a-i*1) + "  " * (i-1))
        print("* " * (a-i))

# left inverted hollow triangle
def leftinvertedhollowtriangle():
    a = int(input("Enter num: "))
    for i in range(a):
        if i == 0 or i == a-1:
            print("* " * (a-i))
        else:
            print("* " + "  " * (a-i-2) + "* ")

# right inverted triangle 
def rightinvertedtriangle():
    a = int(input("Enter num: "))
    for i in range(a):
        print("  " * (i) + "* " * (a-i))



# right inverted hollow triangle
def rightinvertedhollowtriangle():
    a = int(input("Enter num: "))
    for i in range(a):
        if i == 0 or i == a-1:
            print("  " * i + "* " *(a-i))
        else:
            print("  " * i + "* " + "  " * (a-i-2) + "* ")

# pyramid
def pyramid():
    a = int(input("Enter num: "))
    for i in range(a):
        print("  " * (a-i-1) + "* " * (i*2+1))

        
# hollow pyramid
def hollowPyramid():
    a = int(input("Enter num: "))
    for i in range(a):
        if(i == 0 or i == a-1):
            print("  " *(a-i-1) + "* " * (i * 2 + 1))
        else:
            print("  " *(a-i-1) + "* " + "  " *(i*2-1) + "* " )

# inverted pyramid
def invertedpyramid():
    a = int(input("Enter num: "))
    for i in range(a):
        print( "  " * (i) + "* " * (((a*2-1)-(i*2))))

# # inverted hollow pyramid
# def invertedhollowpyramid():
#     a = int(input("Enter num: "))
#     for i in range(a):
#         if i == 0 or i == a-1:
#             print("  " * i + "* " *((a*2-1)-i*2))
#         else:
#             print("  " * i + "* " + "  " * ((a*2) - i*2) + "* ")
# invertedhollowpyramid()

# diamond
def diamond():
    a = int(input("Enter num: "))
    for i in range(a):
        print("  " * (a-i-1) + "* " * (i*2+1))
    for j in range(1,a):
        print("  " * (j) + "* " * (j))

# diamond()