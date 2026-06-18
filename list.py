# ==========================================================
# PYTHON LIST PROGRAMS - PRACTICE REFERENCE
# ==========================================================


# ==========================================================
# 1. FIND DUPLICATE ELEMENTS IN A LIST
# ==========================================================

numbers = [1, 2, 3, 4, 5, 1, 2, 3, 8, 7]
duplicates = []

# count() returns how many times an element occurs
for item in numbers:
    print(item, "->", numbers.count(item))

print(numbers)

# set() removes duplicates
print(set(numbers))

for item in numbers:
    if numbers.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print("Duplicate Elements:", duplicates)


# ---------------- METHOD 2 ----------------

print("\nMethod 2")

duplicates = []

print(numbers)
print(set(numbers))

for item in set(numbers):
    if numbers.count(item) > 1:
        duplicates.append(item)

print("Duplicate Elements:", duplicates)



# ==========================================================
# 2. PRINT ONLY EVEN NUMBERS FROM A LIST
# ==========================================================

numbers = [1,2,3,4,5,6,7,8,9,10]

for item in numbers:
    if item % 2 == 0:
        print(item)



# ==========================================================
# 3. GET LIST INPUT FROM USER
# ==========================================================

# ---------------- METHOD 1 ----------------

numbers = []

for i in range(int(input("Enter number of elements: "))):
    numbers.append(int(input()))

print(numbers)


# ---------------- METHOD 2 ----------------

n = int(input("Enter number of elements: "))

# Creates a list with n zeros
numbers = [0] * n

for i in range(n):
    numbers[i] = int(input())

print(numbers)



# ==========================================================
# 4. FIND LARGEST AND SMALLEST ELEMENT
# ==========================================================

numbers = [1, 3, 45, 23, 45, 2, 34]

# Built-in functions
print(min(numbers))
print(max(numbers))
print(min(numbers), max(numbers))


# ---------------- METHOD 2 (WITHOUT BUILT-IN FUNCTIONS) ----------------

numbers = [1, 3, 45, 23, 45, 2, 34]

largest = numbers[0]
smallest = numbers[0]

for item in numbers:

    if item > largest:
        largest = item

    if item < smallest:
        smallest = item

print("Largest :", largest)
print("Smallest:", smallest)



# ==========================================================
# 5. COUNT HOW MANY TIMES A NUMBER APPEARS
# ==========================================================

numbers = [1, 2, 3, 2, 4, 3, 4, 5, 1, 2]

# Built-in method
print(numbers.count(3))

for item in numbers:
    print(item)


# ---------------- METHOD 2 (WITHOUT BUILT-IN FUNCTION) ----------------

count = 0
target = int(input("Enter Number: "))

for item in numbers:
    if target == item:
        count += 1

print("Count =", count)



# ==========================================================
# 6. CREATE A NEW LIST WITH SQUARES OF ELEMENTS
# ==========================================================

numbers = [1, 2, 3, 4]

# Method 1
for item in numbers:
    print(item ** 2)


# Method 2 - List Comprehension
print([x ** 2 for x in numbers])



# ==========================================================
# 7. CHECK WHETHER A NUMBER EXISTS IN A LIST
# ==========================================================

numbers = [1, 3, 2, 4, 5]

target = int(input("Enter Number: "))

# ---------------- METHOD 1 ----------------

for item in numbers:

    if target == item:
        print("Number exists in the list")
        break

else:
    print("Number does not exist in the list")


# ---------------- METHOD 2 ----------------

print("Exists" if target in numbers else "Doesn't Exist")


# ---------------- NORMAL METHOD ----------------

print(4 in numbers)

if target in numbers:
    print("Exists")
else:
    print("Not Exists")



# ==========================================================
# 8. FIND THE FIRST DUPLICATE ELEMENT
# ==========================================================

numbers = [4, 5, 1, 2, 3, 8, 7, 5]

duplicates = []

for item in numbers:

    if numbers.count(item) > 1:
        duplicates.append(item)
        break

print("First Duplicate:", duplicates)


# ---------------- METHOD 2 (WITHOUT count()) ----------------

numbers = [1, 2, 3, 4, 1, 2, 3, 4, 2]

length = len(numbers)
found = False

for i in range(length):

    for j in range(i + 1, length):

        if numbers[i] == numbers[j]:
            print("First Duplicate:", numbers[i])
            found = True
            break

    if found:
        break