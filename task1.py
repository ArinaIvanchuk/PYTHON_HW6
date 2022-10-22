# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих 
# на нечётной позиции.

print(sum([list[i] for i in range(len(list)) if i % 2]))

#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

print(sum([int(i) for i in input("Input some number: ") if i.isdigit()]))


#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

user_str = 'абв хеллоу ворлд кукумбер абвкукуруза'
print(list(filter(lambda x: 'абв' not in x, user_str.split())))

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import itertools
k = randint(1, 4)
def get_numbers(k):
    numb = [randint(1,10) for i in range(k+1)]
    return numb

def create_polynom(k, numb):
    var = ['*x^']*(k-1) + ['*x']
    poly = [[a, b, c] for a, b, c in itertools.zip_longest(numb, var, range(k, 1, -1), fillvalue=' ') if a != 0]
    for x in poly:
        x.append('+')
    poly = list(itertools.chain(*poly))
    poly[-1] = '= 0'
    return ''.join(map(str, poly)).replace(' 1*x', ' x')

numbers = get_numbers(k)
polynom_1 = create_polynom(k, numbers)
print(polynom_1)

with open('Polynomial.txt', 'w') as data:
    data.write(polynom_1)

numbers = get_numbers(k)
polynom_2 = create_polynom(k, numbers)
with open('Polynomial2.txt', 'w') as data:
    data.write(polynom_2)
