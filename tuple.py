# Tuple is immutable
my_tuple = (1, 2, 'test', 3.14, False, 'Hello World')
print(my_tuple)

new_tuple = tuple([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(new_tuple)

one_elem_tuple = (1, )

print(one_elem_tuple)

# print(tuple.count(new_tuple, 1))

# for x in new_tuple:
#     print(x)

if 'testtt' in new_tuple: print('1 is in the tuple')
else: print('1 is not in the tuple')

print(new_tuple.__contains__(1))

print(list(new_tuple))

another_new_tuple = new_tuple[1::2]
print(another_new_tuple)

rev_tuple = another_new_tuple[::-1]
print(rev_tuple)

print(list(reversed(new_tuple)))





test_tuple = (1, 2, 3, 4, 5, 6)

first, second, *last = test_tuple

print(first, second, last)

#List larger than tuple, maybe more efficient to iterate over tuple than list


import timeit

# Function to create a list and a tuple
def create_list():
    return [1, 2, 3, 4, 5]

def create_tuple():
    return (1, 2, 3, 4, 5)

# Measure the time it takes to create a million instances of a list
list_time = timeit.timeit('create_list()', globals=globals(), number=1000000)

# Measure the time it takes to create a million instances of a tuple
tuple_time = timeit.timeit('create_tuple()', globals=globals(), number=1000000)

print(f"Time taken to create a million instances of a list: {list_time:.6f} seconds")
print(f"Time taken to create a million instances of a tuple: {tuple_time:.6f} seconds")


