# square
def square():
    # a = int(input('Enter num: '))
    a = get_number()
    for i in range(a):
        print("* " * a)

# hollow square
def hollowsquare():
    # a = int(input('Enter num: '))
    a = get_number()
    for i in range(a):
        if i == 0 or i == a-1:
            print("* " * a)
        else:
            print("* " + "  " * (a-2) + "* ")

# left triangle
def lefttriangle():
    # a = int(input('Enter num: '))
    a = get_number()
    for i in range(1,a+1):
        print("* " * i)

# hollow left triangle
def hollowlefttriangle():
    # a = int(input('Enter num: '))
    a = get_number()
    for i in range(1,a+1):
        if i == 1 or i == a:
            print("* " * i)
        else:
            print("* " + "  " * (i - 2) + "* ")

# right triangle
def righttriangle():
    # a = int(input('Enter num: '))
    a = get_number()
    for i in range(a):
        print("  " * (a-i-1) + "* " * (i+1))

# hollow right triangle 
def hollowrighttriangle():
    # a = int(input("Enter num: "))
    a = get_number()
    for i in range(a):
        if i == 0 or i == a-1:
            print("  " * (a-i-1) + "* " * (i+1))
        else:
            print("  " * (a-i-1) + "* " + "  " *(i-1) + "* ")

# left inverted triangle
def leftinvertedtriangle():
    # a = int(input("Enter num: "))
    a = get_number()
    for i in range(a):
        # print("* " * (a-i*1) + "  " * (i-1))
        print("* " * (a-i))

# left inverted hollow triangle
def leftinvertedhollowtriangle():
    # a = int(input("Enter num: "))
    a = get_number()
    for i in range(a):
        if i == 0 or i == a-1:
            print("* " * (a-i))
        else:
            print("* " + "  " * (a-i-2) + "* ")

# right inverted triangle 
def rightinvertedtriangle():
    # a = int(input("Enter num: "))
    a = get_number()
    for i in range(a):
        print("  " * (i) + "* " * (a-i))



# right inverted hollow triangle
def rightinvertedhollowtriangle():
    # a = int(input("Enter num: "))
    a = get_number()
    for i in range(a):
        if i == 0 or i == a-1:
            print("  " * i + "* " *(a-i))
        else:
            print("  " * i + "* " + "  " * (a-i-2) + "* ")

# pyramid
def pyramid():
    # a = int(input("Enter num: "))
    a = get_number()
    for i in range(a):
        print("  " * (a-i-1) + "* " * (i*2+1))

        
# hollow pyramid
def hollowPyramid():
    # a = int(input("Enter num: "))
    a = get_number()
    for i in range(a):
        if(i == 0 or i == a-1):
            print("  " *(a-i-1) + "* " * (i * 2 + 1))
        else:
            print("  " *(a-i-1) + "* " + "  " *(i*2-1) + "* " )

# inverted pyramid
def invertedpyramid():
    # a = int(input("Enter num: "))
    a = get_number()
    for i in range(a):
        print( "  " * (i) + "* " * (((a*2-1)-(i*2))))

# inverted hollow pyramid
def invertedhollowpyramid():
    # a = int(input("Enter num: "))
    a = get_number()
    for i in range(a):
        if i == 0 or i == a-1:
            print("  " * i + "* " *((a*2-1)-i*2))
        else:
            print("  " * i + "* " + "  " * ((a*2-1) - ((i*2)+2)) + "* ")


# diamond
def diamond():
    # a = int(input("Enter num: "))
    a = get_number()
    for i in range(a):
        print("  " * (a-i-1) + "* " * (i*2+1))
    for j in range(1,a):
        print("  " * (j) + "* " * ((a*2-1) - j*2))

# diamond method 2
def diamond2():
    # a = int(input("Enter num: "))
    a = get_number()
    for i in range(a):
        print("  " *(a-i-1) + "* " * (i * 2 + 1))
    for j in range(1,a):
        print("  " * j + "* " * (a - j) + "* " *(a - j - 1))


# hollow diamond
def hollowdiamond():
    # a = int(input("Enter num: "))
    a = get_number()
    for i in range(a):
        if i == 0:
            print("  " * (a-i-1) + "* " * (i*2+1))
        else:
            print("  " * (a-1-i) + "* " + "  " * (i*2-1) + "* ")
    for j in range(1,a):
        if j == a-1:
            print("  " *j + "* " * ((a*2-1)-(j*2)))
        else:
            print("  " * j + "* " + "  " * ((a*2-3)-(j*2)) + "* ")

# parallelogram
def parallelogram():
    # a = int(input("Enter num: "))
    a = get_number()
    for i in range(a):
        print("  " * i + "* " * a)

# hollow parallelogram
def hollowparallelogram():
    # a = int(input("Enter num: "))
    a = get_number()
    for i in range(a):
        if i == 0 or i == a-1:
            print("  " * i + "* " * a)
        else:
            print("  " * i + "* " + "  " * (a-2) + "* ")

# inverted parallelogram
def invertedparallelogram():
    # a = int(input("Enter num: "))
    a = get_number()
    for i in range(a):
        print("  " * (a-i-1) + "* " * a)

# inverted hollow parallelogram
def invertedhollowparallelogram():
    # a = int(input("Enter num: "))
    a = get_number()
    for i in range(a):
        if i == 0 or i == a-1:
            print("  " * (a-1-i) + "* " * a)
        else:
            print("  " * (a-1-i) + "* " + "  " * (a-2) + "* ")

# get number as function
def get_number():
    while True:
        try:
            a = int(input("Enter num: "))

            if a <= 0:
                print("Enter a positive number.")
                continue

            return a

        except ValueError:
            print("Invalid input. Please enter a positive integer.")

        except KeyboardInterrupt:
            print("\nInput cancelled. Please try again.")


def patternsmenu():
    print("********Welcome to Patterns Worlds!!!********")

    while True:
        print(
        "1. Square\n2. Hollow Square\n3. Left Triangle\n"
        "4. Hollow Left Triangle\n5. Right Triangle\n"
        "6. Hollow Right Triangle\n7. Left Inverted Triangle\n"
        "8. Left Inverted Hollow Triangle\n9. Right Inverted Triangle\n"
        "10. Right Inverted Hollow Triangle\n11. Pyramid\n"
        "12. Hollow Pyramid\n13. Inverted Pyramid\n"
        "14. Inverted Hollow Pyramid\n15. Diamond - Method 1\n"
        "16. Diamond - Method 2\n17. Hollow Diamond\n"
        "18. Parallelogram\n19. Hollow Parallelogram\n"
        "20. Inverted Parallelogram\n21. Inverted Hollow Parallelogram\n22. Exit"
    )
        print("\n--------------------------------------------------------")
        try:
            choice = int(input("\n Enter Choice: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        except KeyboardInterrupt:
            print("\n Input cancelled by user")
            return None
        if choice < 1 or choice > 22:
            print("Please enter a choice between 1 and 22.")
            continue
        
        match choice:
            case 1:
                print("\nSquare\n")
                square()
            case 2:
                print("\nHollow Square\n")
                hollowsquare()
            case 3: 
                print('\nLeft Triangle\n')
                lefttriangle()
            case 4: 
                print('\nHollow Left Triangle\n')
                hollowlefttriangle()
            case 5:
                print("\nRight Triangle\n")
                righttriangle()
            case 6:
                print("\nHollow Right Triangle\n")
                hollowrighttriangle()
            case 7:
                print("\nLeft Inverted Triangle\n")
                leftinvertedtriangle()
            case 8:
                print("\nLeft Inverted Hollow Triangle\n")
                leftinvertedhollowtriangle()
            case 9:
                print("\nRight Inverted Triangle\n")
                rightinvertedtriangle()
            case 10:
                print("\nRight Inverted Hollow Triangle\n")
                rightinvertedhollowtriangle()
            case 11:
                print("\nPyramid\n")
                pyramid()
            case 12:
                print("\nHollow Pyramid\n")
                hollowPyramid()
            case 13:
                print("\nInverted Pyramid\n")
                invertedpyramid()
            case 14:
                print("\nInverted Hollow Pyramid\n")
                invertedhollowpyramid()
            case 15:
                print("\nDiamond Method 1\n")
                diamond()
            case 16:
                print("\nDiamond Method 2\n")
                diamond2()
            case 17:
                print("\nHollow Diamond\n")
                hollowdiamond()
            case 18:
                print("\nParallelogram\n")
                parallelogram()
            case 19:
                print("\nHollow Parallelogram\n")
                hollowparallelogram()
            case 20:
                print("\nInverted Parallelogram\n")
                invertedparallelogram()
            case 21:
                print("\nInverted Hollow Parallelogram\n")
                invertedhollowparallelogram()
            case 22:
                print("\n*********Thank you********")
                break
            

patternsmenu()