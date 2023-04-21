list_1 = []
print(list_1)
for i in range(5): # 5 итераций 
    list_1.append(i) # добавляем при каждой итерации в конец списка следующее число
    print(list_1)

list_1 = [3, -5, 7, 2, -6, 12]
for i in range(len(list_1)):
    print(list_1[i], end=' ') # вывод каждого элемента списка