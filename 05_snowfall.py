# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные


# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
N = 20
coord_list = []
length_list = []
factor_list = []
for i in range(N):
    fill = [sd.random_number(0, 1200), sd.random_number(600,900)]
    coord_list.append(fill)
    fill = sd.random_number(10, 50)
    length_list.append(fill)
    fill = [sd.random_number(40, 70) / 100, sd.random_number(30, 50) / 100, sd.random_number(30, 90)]
    factor_list.append(fill)
while True:

    sd.clear_screen()
    for i in range(N):
        x, y = coord_list[i]
        if x < 0:
            x = sd.random_number(0, 1200)
        if y <= 0:
            y = sd.random_number(600,900)
            x=sd.random_number(0, 1200)
        point = sd.get_point(x, y)
        a, b, c = factor_list[i]
        sd.snowflake(center=point, length=length_list[i], factor_a=a, factor_b=b, factor_c=c)
        x += sd.random_number(-10, 10)
        y -= sd.random_number(0, 50)
        coord_list[i] = x, y


    sd.sleep(0.1)
    if sd.user_want_exit():
         break

sd.pause()
