# ======================================
# LIST COMPREHENSION, FILTER, MAP, ZIP,
# ANY, and ALL
# ======================================


# --------------------------------------
# 1. List Comprehension & filter()
# --------------------------------------

list1 = [1, 2, 3, 4]

# Even numbers using List Comprehension
print([x for x in list1 if x % 2 == 0])

# Even numbers using filter()
print(list(filter(lambda x: x % 2 == 0, list1)))

# Output:
# [2, 4]
# [2, 4]


# --------------------------------------
# 2. Odd Numbers
# --------------------------------------

# Odd numbers using List Comprehension
print([x for x in list1 if x % 2])

# Odd numbers using filter()
print(list(filter(lambda x: x % 2, list1)))

# Output:
# [1, 3]
# [1, 3]


# --------------------------------------
# 3. Square of Numbers
# --------------------------------------

# Squares of odd numbers only
print([x**2 for x in list1 if x % 2])

# Squares of all numbers using map()
print(list(map(lambda x: x**2, list1)))

# Output:
# [1, 9]
# [1, 4, 9, 16]


# ======================================
# ZIP FUNCTION
# ======================================

twodlist = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

twoDlist = [[1, 2],
            [4, 6],
            [8, 9]]

twolist = [[1, 2],
           [4],
           [8, 9]]

# Transpose of a 3x3 matrix
print(list(zip(*twodlist)))

# Output:
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]


# Transpose of a 3x2 matrix
print(list(zip(*twoDlist)))

# Output:
# [(1, 4, 8), (2, 6, 9)]


# zip() stops at the shortest list
print(list(zip(*twolist)))

# Output:
# [(1, 4, 8)]


# ======================================
# ANY FUNCTION
# ======================================

# Returns True if at least one value is True

print(any([x % 2 == 0 for x in [2, 4, 5]]))
print(any([x % 2 == 0 for x in [2, 4, 6]]))

# Output:
# True
# True


# ======================================
# ALL FUNCTION
# ======================================

# Returns True only if every value is True

print(all([x % 2 == 0 for x in [2, 4, 5]]))
print(all([x % 2 == 0 for x in [2, 4, 6]]))

# Output:
# False
# True