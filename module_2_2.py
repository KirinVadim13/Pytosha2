# создаём переменные для ввода трёх целых чисел
first = int(input("Первое число: "))
second = int(input("Второе число: "))
third = int(input("Третье число: "))

# формулы для проверки равенства чисел
if first == second and second == third and first == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
elif not first == second and not second == third and not first == third:
    print(0)
# или сразу исключаем 11 строку и завершаем логическую формулу
# не иcпользуя оператор not
else:
    print(0)