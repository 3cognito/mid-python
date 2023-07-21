my_set = {1, 2, 3, 3, 4, 4, 5, 5, 5,5 }

print(my_set)

my_set.add(6)
print(my_set)

new_set = set([9, 9, 9, 8])
print(new_set)

# Sets are unordered and mutable

new_set.discard(9)
print(new_set)


# new_set.pop()
new_set.clear()

print(new_set)

# Iteration is same as in other iterables


odd_numbers = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
even_numbers = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}

# Union

u = odd_numbers.union(even_numbers)
i = odd_numbers.intersection(prime_numbers)
d = odd_numbers.difference(prime_numbers)
sd = odd_numbers.symmetric_difference(prime_numbers)
print(u, i, d, sd)


# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Using update method
set1.update(set2)
print("After update:", set1)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Create two sets again to demonstrate difference_update and intersection_update
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Using difference_update method
set1.difference_update(set2)
print("After difference_update:", set1)  # Output: {1, 2, 3}

# Create two sets again to demonstrate difference_update and intersection_update
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Using intersection_update method
set1.intersection_update(set2)
print("After intersection_update:", set1)  # Output: {4, 5}





set1 = {1, 2, 3, 4, 5}
set2 = {1, 2}
set3 = {1, 2, 9}

print(set2.issubset(set1))
print(set1.issuperset(set2))
print(set1.isdisjoint(set3)) #No similar elements




# To copy a set use the copy method or the set constructor wrapped around the original set
# The add method also works like lists and tuples


a = frozenset([1, 2, 3, 4, 5])
print(a)
# Frozen sets are immmutable