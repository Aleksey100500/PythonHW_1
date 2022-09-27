# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между 
# ними в 2D пространстве. https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1

# out
# 5.099

xyzA = ['Xa', 'Ya']
xyzB = ['Xb', 'Yb']

numbersA = []
numbersB = []

for i in range(2):
    numbersA.append(int(input(f'Введите координату {xyzA[i]}: ')))
    numbersB.append(int(input(f'Введите координату {xyzB[i]}: ')))

result = (((numbersB[0] - numbersA[0]) ** 2) + ((numbersB[1] - numbersA[1]) ** 2)) ** 0.5

print(f'Расстояние между точками A({numbersA[0]}, {numbersA[1]}) и B({numbersB[0]}, {numbersB[1]}) равно {round(result, 3)}')