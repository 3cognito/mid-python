sample_dict = {'a': 1, 'b': 2, 'c': 3}

print(sample_dict['a'])
sample_dict.pop('a')
sample_dict['d'] = 4
sample_dict['b'] = 5
del sample_dict['c']
sample_dict.popitem()
print(sample_dict)

test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
if 1 in test_dict: print('yes')

try: 
    if 'b' in test_dict: print('yes')
except: print('no')


# for key in test_dict:
#     print(key, test_dict[key])


# for key in test_dict.values():
#     print(key)

# for key in test_dict.keys():
#     print(key)


#Dictionaries are unordered



test_dict_copy = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
new_dict = test_dict_copy.copy()
new_dict_2 = dict(test_dict_copy)

print(new_dict, new_dict_2)

another_dict = dict(a=1, b=2, c=3, d=5)
print(another_dict)

another_dict.update(dict(a=1, b=2, c=3, d=4, e=5))
print(another_dict)







funny_dict = {2: 'a', 3: 'b', 4: 'c', 5: 'd', 6: 'e'}
another_funny_dict = {(1, 2): 'a', (3, 4): 'b', ('test', 6): 'c'}

# Any immutable object can be a key - lists can not be used as keys

print(funny_dict, another_funny_dict)









