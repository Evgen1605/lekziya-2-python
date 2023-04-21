# Словари
# Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.
# В списках в качестве ключа используется индекс элемента. В словаре для определения элемента используется значение ключа(строка, число).

d = {} # пустой словарь
d = dict() # пустой словарь
d['q'] = 'qwerty'  # q- это ключ qwerty- значение
print(d)  # {'q': 'qwerty'}
d['w'] = 'asdf'
print(d)  # {'q': 'qwerty', 'w': 'asdf'}
print(d['q'])  # qwerty
 
dictionary = {} # пустой словарь
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary)  # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться
print(dictionary['up'])  # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left'])  # ⇐
# print(dictionary['type'])  # KeyError: 'type'
del dictionary['left']  # удаление элемента

for item in dictionary:  # for (k,v) in dictionary.items():
  print('{}: {}'.format(item, dictionary[item]))
#  up: ↑
# down: ↓
# right: →
