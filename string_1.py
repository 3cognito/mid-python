my_string = 'test string'
multi_line_string = '''this is a
multi line string'''

# backslash can also be used for escaping
# immutable
print(my_string[3])

sub = my_string[1:5]
print(sub) # Default behavior of slicing is to include the first index and exclude the last index, if first is excluded, it starts from the beginning, if last is excluded, it goes to the end, there is also a third optional step arg
print(my_string[::2]) # step arg

concat_str = my_string + ' ' + multi_line_string
print(concat_str)

# Strings are iterable so the for in loop works

if 'test' in my_string:
    print('test is in the string')

print(my_string.__contains__('test')) # Same as above

white_spc = '   test   '
print(white_spc.strip()) # Removes whitespace from beginning and end of string
print(my_string.lower())
print(my_string.upper())
print(my_string.startswith('test'))
print(my_string.endswith('test'))
print(my_string.find('t')) # Returns index of first occurrence of substring
print(my_string.replace('test', 'new test'))
print(my_string.count('t')) # Returns number of occurrences of substring
print(my_string.split(' ')) # Returns a list of substrings separated by the delimiter


ex_list = ['I', 'am', 'a', 'list']
print('😂'.join(ex_list)) # Joins list elements with a delimiter






var = 'This is a long sample %s string' % 'test'
print(var)
var = 'This is a long sample %d string' % 44444
print(var)
var = 'This is a long sample %.3f string' % 0.99
print(var)





var = 'This is a long sample {} string'.format('test')
print(var)
var = 'This is a long sample {} string {}'.format(44444, 'test')
print(var)



fill1 = 'test'
fill2 = 44444

var = f'This is a long sample {fill1} string {fill2}' # Similar to above but more readable and also simlilar to javascript's template literals
print(var)





