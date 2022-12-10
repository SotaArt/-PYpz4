# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#     *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x²

from random import randint
import itertools

k = randint(2, 7)

def get_ratios(k):
    ratios = [randint(0, 10) for i in range (k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10)
    return ratios

def get_megafaka(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    megafaka = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in megafaka:
        x.append(' + ')
    megafaka = list(itertools.chain(*megafaka))
    megafaka[-1] = ' = 0'
    return "".join(map(str, megafaka)).replace(' 1*x',' x')


ratios = get_ratios(k)
megaf1 = get_megafaka(k, ratios)
print(megaf1)

with open('big-megafaka.txt', 'w') as data:
    data.write(megaf1)


# Второй многочлен для следующей задачи:

k = randint(2, 5)

ratios = get_ratios(k)
megaf2 = get_megafaka(k, ratios)
print(megaf2)

with open('big-megafaka2.txt', 'w') as data:
    data.write(megaf2)