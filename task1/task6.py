# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

d_week = int(input('Введите номер дня недели (число от 1 до 7): '))

if d_week > 7 or d_week < 1:
	print('Ошибка ввода! Неверно введён номер дня недели!')
	exit()

if d_week == 6 or d_week == 7:
	print(d_week, '-> да')
else:
	print(d_week, '-> нет')