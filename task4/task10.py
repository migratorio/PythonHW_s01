# 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

coord_list = []
point_list = ['X точки A: ', 'Y точки A: ', 'X точки B: ', 'Y точки B: ']
for i in range(4):
    print('Введите координату ', end=' ')
    print(point_list[i], end=' ')
    x = int(input())
    coord_list.append(x)
  
res = math.sqrt((coord_list[2] - coord_list[0])**2 + (coord_list[3] - coord_list[1])**2)
print('A(', coord_list[0], ',',coord_list[1], '); B(', coord_list[2], ',',coord_list[3], ') -> ', round(res, 3))

# такое решение сложнее, чем поочерёдный ввод координат, но решать было интереснее :)