my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]#создаём список
dl_spiska = len(my_list)#длина данных списка, граница списка
#print(dl_spiska) #проверяем для себя, равно 12

index = 0 # создаём переменную и её значение

while index < dl_spiska: # задаём цикл пока переменная index меньше длины списка
    number = my_list[index] # число из списка по индексу
    #print(my_list[index]) проверка для себя
    if number < 0:
        continue
    if number > 0:
        print(number)
    index = int(index + 1) # в каждом цикле увеличиваем значение переменной на +1



