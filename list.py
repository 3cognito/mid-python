myList = ['test', False, 3.14, 42, 'Hello World']

print(myList[-3]) 

for i in myList:
    print(i)

test_var = 'test'

if test_var in myList:
    print('test is in the list')

myList.remove(False)

print(myList)

myList.reverse()

print(myList)

test_str_list = ['test', 'test5', 'test3']

# print(sorted(test_str_list) * 5)

# another_list = myList + test_str_list
# print(another_list)

# test_slice = another_list[1::2]
# print(test_slice)


copy_list = test_str_list.copy()
print(copy_list)


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_num_list = [i * 2 for i in num_list if i % 2 == 0]
print(new_num_list)