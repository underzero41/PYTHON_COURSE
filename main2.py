# list_1 = []
# list_2 = list()
# list_3 = list[1,2,3,4,5]

# for i in list_3:
#     print(i)

# print(len(list_3))
# print(list_3[1])

# list_1 = [1,5]
# print(*list_1)
# list_1.append(8)
# print(*list_1)

# list_1 = []
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# Delete last element

# list_1 =[12, 2, -8, 3, 4, -5]
# print(*list_1)
# print(list_1.pop())
# print(*list_1)
# print(list_1.pop())
# print(*list_1)
# print(list_1.pop())
# print(*list_1)

# # Delete awsome element in list

# list_1 = [12, 2, -8, 3, 4, -5]
# print(list_1)
# print(list_1.pop(0))
# print(*list_1)

# # Add element to list
# list_1 = [12, 2, -8, 3, 4, -5]
# print(*list_1)
# print(list_1.insert(2, 11))
# print(*list_1)


# list_1 = [12, 2, -8, 3, 4, -5, 2, 4, 5, 6, 7, -5]
# print(list_1[0])
# print(list_1[1])
# print(list_1[len(list_1)-1])
# print(list_1[-5])
# print(list_1[:])
# print(list_1[:2])
# print(list_1[len(list_1)-2:])
# print(list_1[2:5])
# print(list_1[6:-18])
# print(list_1[0:len(list_1):6])
# print(list_1[::6])

# # Kortezh

# t = ()
# print(type(t))
# t = (1, 5, 3,)
# print(type(t))

# v = [1, 8, 9]
# print(type(v))

# v = tuple(v)
# print(type(v))

# # a = 1
# # b = 2
# # a, b = 1, 2
# a, b, c = v

# print(a, b, c)

# t = (1,2,3,4,5,)
# print(t[1])
# for i in t:
#     print(i)

# for i in range(len(t)):
#     print(t[i])


# Dictionary

# d = {}
# d = dict
# d['q'] = 'qwerty'
# print(d)
# d['w'] = 'werty'
# print(d)

# dictionary = {}
# dictionary = {'up': 'u', 'left': 'l', 'right': 'r', 'down': 'd'}
# print(dictionary)
# print(dictionary['up'])
# print(dictionary['down'])
# print(dictionary['left'])
# print(dictionary['right'])
# dictionary['left'] = '<-'
# print(dictionary['left'])
# del dictionary['left']
# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))

# dictionary[895] = 9888
# print(dictionary)

# Множества

# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('red')
# print(colors)
# colors.add('grey')
# print(colors)
# colors.remove('red')
# print(colors)
# colors.discard('red')
# print(colors)
# colors.clear()
# print(colors)

# q = set()

# # Операции со множествами
# a = {1, 2, 3, 4, 5, 6, 7}
# b = {9, 8, 7, 6, 5, 4, 3}
# c = a.copy()
# u = a.union(b)
# i = a.intersection(b)
# dl = a.difference(b)
# dr = b.difference(a)
# q = a.union(b).difference(a.intersection(b))

# # Замороженное множество

# a = {1, 8, 6}
# b = frozenset(a)

# List Comprehension

# list_1 = [exp for item in iterable]
# list_1 = [exp for item in iterable(if conditional)]
# list_1 = [i for i in range(1, 101)]
# print(list_1)
# list_2 = [i for i in range(1, 101) if i % 2 == 0]
# print(list_2)
# list_3 = [(i, i) for i in range(1, 101) if i % 2 == 0]
# print(list_3)
# list_4 = [i*2 for i in range(1,101) if i % 2 == 0]
# print(list_4)