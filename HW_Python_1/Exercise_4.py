# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*

# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти

chetvert = int(input('Введите номер четверти: '))

if chetvert <=4 and chetvert > 0:
    if chetvert == 1:
        print('x > 0 , y > 0')
    elif chetvert == 2:
        print('x < 0, y > 0')
    elif chetvert == 3:
        print('x < 0, y < 0')
    else:
        print('x > 0, y < 0')
else:
    print('Нет такой четверти')