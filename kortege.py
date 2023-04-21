# Кортеж
# Кортеж — это неизменяемый список.
# Тогда для чего нужны кортежи, если их нельзя изменить? В случае защиты каких-либо данных от изменений(намеренных или случайных). Кортеж занимает меньше места в памяти и работают быстрее, по сравнению со списками

t = ()  # создание пустого кортежа
print(type(t))  # <class 'tuple'>

t = (1, 2, 3,)  # для создания кортежа необходимо поставить в конце ,
print(type(t))  # <class 'tuple'>

v = [4, 5, 8]
print(v)  # [1, 2, 3]
print(type(v))  # <class 'list'>

# преобразовываем список в кортеж
v = tuple(v)
print(v)  # (1, 2, 3)
print(type(v))  # <class 'tuple'>

a, b, c = v # множественное присваивание
print(a, b, c) # выводится три переменных(сделали распаковку кортежа)

colors = ['red', 'green', 'blue']
print(colors)  # ['red', 'green', 'blue']
# преобразовываем список в кортеж
t = tuple(colors)
print(t)  # ('red', 'green', 'blue')
t = tuple(['red', 'green', 'blue'])
print(t[0])  # red
print(t[2])  # blue

for e in t:
  print(e)  # red green blue

# t[0] = 'black'  # TypeError: 'tuple' object does not support(нельзя изменять кортеж)

# распаковываем кортеж в независимые переменные
t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))  # r:red g:green b:blue
 
