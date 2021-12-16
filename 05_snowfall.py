# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

# N = 20
# coord_list = []
# length_list = []
# for i in range(N):
#     fill = [sd.random_number(0, 1200), 600]
#     coord_list.append(fill)
#     fill = sd.random_number(10,100)
#     length_list.append(fill)
# #print(coord_list)
# # Пригодятся функции
# # sd.get_point()
# # sd.snowflake()
# # sd.sleep()
# # sd.random_number()
# # sd.user_want_exit()
#
#
# while True:
#     sd.clear_screen()
#     for i in range(N):
#         x, y = coord_list[i]
#         if x<0:
#             x=sd.random_number(0,1200)
#         if y<0:
#             y=600
#
#         point = sd.get_point(x, y)
#         sd.snowflake(center=point, length=length_list[i])
#         x += sd.random_number(-10, 10)
#         y -= sd.random_number(0, 20)
#         coord_list[i] = x, y
#
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
#
# sd.pause()

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
for i in range(N):
    fill = [sd.random_number(0, 1200), 700]
    coord_list.append(fill)
    fill = sd.random_number(10, 100)
    length_list.append(fill)
while True:

    sd.clear_screen()
    # for j in range(N):
    #     x0, y0 = coord_list[j]
    #     if y0 < 10:
    #         point0 = sd.get_point(x0, 50)
    #         sd.snowflake(center=point0, length=length_list[j])

    for i in range(N):

        x, y = coord_list[i]
        if x < 0:
            x = sd.random_number(0, 1200)
        if y <= 0:
            y=700
        point = sd.get_point(x, y)

        sd.snowflake(center=point, length=length_list[i])
        x += sd.random_number(-10, 10)
        y -= sd.random_number(0, 50)
        coord_list[i] = x, y
    if y<0:
        continue
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
