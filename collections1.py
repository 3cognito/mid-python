from collections import Counter, defaultdict, OrderedDict, namedtuple, deque

a = 'aaaaabbbbbccccccccccccc'
my_counter = Counter(a)
print(my_counter) # Creates a dictionary where the unique elements of the string are the keys and the values are the number of occurrences of each element

print(my_counter.items()) # Returns a list of tuples of the form (element, count)
print(my_counter.keys()) # Returns a list of the unique elements
print(my_counter.values()) # Returns a list of the number of occurrences of each element
print(my_counter.most_common(1)) # Returns a list of the n most common elements and their counts


Point = namedtuple('Point', 'x,y')
print(Point(11, 22)) # Creates a tuple with named fields




# Sample list of fruits with colors
fruits = [
    ('apple', 'red'),
    ('banana', 'yellow'),
    ('orange', 'orange'),
    ('grape', 'purple'),
    ('apple', 'green'),
    ('banana', 'green'),
]

# Using defaultdict to group fruits by color
fruits_by_color = defaultdict(list)
print(fruits_by_color)
for fruit, color in fruits:
    fruits_by_color[color].append(fruit)

print(fruits_by_color)


