numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [] # пустой список для простых чисел
not_primes = [] # пустой список для не простых чисел
#print(primes, not_primes) #проверка для себя
# Простые числа - это целое положительное число больше единицы,
# которое не делится без остатка ни на одно другое целое положительное число,
# кроме единицы и самого себя.
for i in numbers:
    if i < 2:
        continue
    is_prime = True
    for x in range(2,i):
        if i % x == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print('Primes: ', primes)
print('Not_Primes: ', not_primes)
