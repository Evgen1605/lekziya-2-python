# Множества
# Множества содержат в себе уникальные элементы, не обязательно упорядоченные.

q = set()  # пустое множество

colors = {'red', 'green', 'blue'}
print(colors)  # {'green', 'blue', 'red'} множества могут выводится в любом порядке

colors.add('red') # add добавляет в множество элемент, но т.к у же есть red, ничего не добавит
print(colors)  # {'red', 'green', 'blue'}
colors.add('grey')
print(colors)  # {'blue', 'green', 'red', 'grey'}

colors.remove('red') # remove удаляет элемент
print(colors)  # {'grey', 'blue', 'green'}
# colors.remove('red')  # KeyError: 'red' ошибка, т.к этого элемента нет (удалили  ранее)

colors.discard('red') # discard проверяет есть ли этот элемент, если нету, то просто пропускает
print(colors)  # {'blue', 'grey', 'green'}

colors.clear() # clear очищает множества
print(colors) # set()
