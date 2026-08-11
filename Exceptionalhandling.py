try:
    num1 = float(input("Enter Num1: "))
    num2 = float(input("Enter Num2: "))
    result = num1/num2
except ValueError:
    print("Only Numbers")
except ZeroDivisionError:
    print("Number can't be zero as divided")
except Exception as error:
    print(type(error).__name__)
else:
    print(result)
finally:
    print("*****THE END*****")
