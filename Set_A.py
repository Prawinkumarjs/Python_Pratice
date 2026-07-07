# ----------------------------
# SET OPERATIONS
# ----------------------------

a = {1, 2, 3, 5}
b = {2, 4, 6, 7}

# Union (Combines all unique elements)
result1 = a.union(b)

# Difference (Elements present in a but not in b)
result2 = a.difference(b)

# Intersection (Common elements)
result3 = a.intersection(b)

# Copy the set
a1 = a.copy()

print("Union:", result1)
print("Difference:", result2)
print("Intersection:", result3)
print("Copy:", a1)


# ----------------------------
# ADDING ELEMENTS
# ----------------------------

# Add a single element
a1.add(8)
print("\nAfter add(8):", a1)

# Add multiple elements
a1.update([22, 23, 25])
print("After update([22, 23, 25]):", a1)


# ----------------------------
# DIFFERENCE UPDATE
# ----------------------------

# Remove all elements that are present in 'a'
a1.difference_update(a)
print("\nAfter difference_update(a):", a1)


# ----------------------------
# INTERSECTION UPDATE
# ----------------------------

c = {1, 2, 3, 5}
c1 = {1, 2, 3, 5, 8, 22, 23, 25}

# Keep only common elements
c1.intersection_update(c)

print("\nAfter intersection_update(c):", c1)
print("Original c:", c)


# ----------------------------
# POP
# ----------------------------

# Removes and returns an arbitrary element
c.pop()
print("\nAfter pop():", c)


# ----------------------------
# DISCARD
# ----------------------------

print("\nBefore discard:", b)

# Removes 4 if present (no error if absent)
b.discard(4)

print("After discard(4):", b)