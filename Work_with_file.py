# def f(x):
#     return x*x
# a = f
# print(a(5))
# print(f(5))

def calc1(a, b):
    return a*b

def calc2(a, b):
    return a*b

def math(op, x, y):
    print(op(x, y))



# def calc1(a, b):
#     return a + b

# calc1 = lambda a, b: a + b         тоже самое что ниже !

math(lambda a, b: a + b , 5, 45)

# ----------------------------------------------------------
# array_1 = [1, 2, 3, 5, 8, 15, 23, 38]

# res =list()

# for i in array_1:
#     if i % 2 == 0:
#         res.append((i, i**2))

# print(res)
print('---------------------------------------')

def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return[x for x in col if f(x)] 

array_1 = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, array_1)
print(res)

res = where(lambda x: x % 2 == 0, res)
print(res)

res = select(lambda x: (x, x**2), res)
print(res)


print('---------------------------------------')

def where(f, col):
    return[x for x in col if f(x)] 

array_2 = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, array_2)
print(res)

res = where(lambda x: x % 2 == 0, res)
print(res)

res = list(map(lambda x: (x, x**2), res))
print(res)

print('---------------------------------------')

# /////////////////////////////////////////
list_1 = [x for x in range(1, 20)]
print(list_1)


list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)

# ------------------------------------------

data = '21 73 18 2 39 21 840 912 83'
# print(data)
# print(type(data))

# data = data.split()
# print(data)

data = list(map(int, data.split()))
print(data)

print('---------------------------------------')


data_2 = [12, 35, 6, 748, 74, 0, 3]
res = list(filter(lambda x: x % 10 == 5, data_2))
print(res)

print('---------------------------------------')




array_2 = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, array_2)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x**2), res))
print(res)


print('---------------------------------------')

# colors = ["red", "888", "blue"]
# data3 = open("file.txt", "a")   # указываем режим в котором будем работать
# data3.writelines(colors)         # разделителей не будет 
# data3.close()

# with open("file.txt", "w") as data3:
#     data3.write("line 1\n")
#     data3.write("line 2\n")


path = "file.txt"
data4 = open("file.txt", "r")
for line in data4:
    print(line)
data4.close()


print('---------------------------------------')


