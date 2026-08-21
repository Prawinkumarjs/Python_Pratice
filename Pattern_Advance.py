# Butterfly
def butterfly():
    a = int(input("Enter num: "))
    for i in range(1,a+1):
        print("* " * i + "  " * ((a*2)-i*2) + "* " * i )
    for j in range(1,a):
        print("* " * (a-j) + "  " * ((j*2)) + "* " * (a-j) )


# hollow butterfly
def hollowbutterfly():
    a = int(input("Enter num: "))
    for i in range(a):
        if i == 0:
            print("* "  + "  " * (a*2) + "* " )
        else:
            print("* " + "  " * (i-1) + "* " + "  " * ((a*2)-(i*2)) + "* " + "  " * (i-1) + "* ")
    for j in range(a+1):
        if j == a:
            print("* " + "  " * (j*2) + "* ")
        else:
            print("* " + "  " * (a-j-1) + "* " + "  " * (j*2) + "* " + "  " * (a-j-1) + "* ")


# X pattern
def xpattern():
    a = int(input("Enter num: "))
    for i in range(a):
        if i == a-1:
            print("  " * i + "* " )
        else:
            print("  " * i + "* " + "  " * ((a*2-2)-(i*2) )+ "* " )

    for j in range(1,a):
            print("  " * (a-j-1) + "* " + "  " * (j*2-1) + "* " )

            


xpattern()

def srixpattern():
    a = int(input("Enter num: "))
    for i in range(a):
        for j in range(a):
            if i==j or i+j==a-1:
                print("* ",end="")
            else:
                print("  ",end="")
        print()

srixpattern()

