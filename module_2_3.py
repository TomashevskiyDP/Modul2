# Домашняя работа по уроку "Стиль кода часть II. Цикл While"

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = 0
while x < len(my_list) and my_list[x] >= 0:
    if my_list[x] > 0:
        print(my_list[x])
    x += 1
