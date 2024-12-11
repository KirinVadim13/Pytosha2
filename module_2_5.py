def get_matrix(n, m, value): # создаём функцию с параметрами
    matrix = [] # создаём пустой список
    for i in range(n): # цикл for для количества строк "матрицы" с размерностью n
        empty_list = [] # создаем переменную "пустой_список"
        for j in range(m): # внутренний цикл for для количества столбцов "матрицы" с размерностью m
            empty_list.append(value) # пополняем в добавленный empty_list значения value
        matrix.append(empty_list) # в "матрицу" добавляем сначения "пустого_списка"
    return matrix # вывод "матрицы"
result1 = get_matrix(2, 2, 10) # проверяем с параметрами
print(result1)
result2 = get_matrix(3, 5, 42) # проверяем с параметрами
print(result2)
result3 = get_matrix(4, 2, 13) # проверяем с параметрами
print(result3)

