# -*- coding: utf-8 -*-

import simple_draw as sd

sd.set_screen_size(1200, 800)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# def draw_branches(start_point, angle, length):
#     if length < 10:
#         return
#     angle_0 = angle + 90
#     angle_1 = angle_0 - 30
#     angle_2 = angle_0 + 30
#     v1 = sd.get_vector(start_point=start_point, angle=angle_1, length=length)
#     v2 = sd.get_vector(start_point=start_point, angle=angle_2, length=length)
#     v1.draw()
#     v2.draw()
#     next_length = length * 0.75
#     draw_branches(start_point=v1.end_point, angle=angle - 30, length=length * 0.75)
#     draw_branches(start_point=v2.end_point, angle=angle + 30, length=length * 0.75)



# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg
# Пригодятся функции
# sd.random_number()
def draw_branches(start_point, angle, length):
    if length < 5:
        return
    angle_0 = angle + 90
    angle_1 = angle_0 - 30
    angle_2 = angle_0 + 30
    v1 = sd.get_vector(start_point=start_point, angle=angle_1, length=length)
    v2 = sd.get_vector(start_point=start_point, angle=angle_2, length=length)
    v1.draw()
    v2.draw()
    next_length = length * 0.75
    random_angle1 = sd.random_number(18, 42)
    random_angle2 = sd.random_number(18, 42)
    random_length1 = sd.random_number(6, 9) / 10
    random_length2 = sd.random_number(6, 9) / 10
    draw_branches(start_point=v1.end_point, angle=angle - random_angle1, length=length * random_length1)
    draw_branches(start_point=v2.end_point, angle=angle + random_angle2, length=length * random_length2)

point = sd.get_point(600, 50)
tree = sd.get_vector(start_point=point, angle=90, length=100)
tree.draw(width=5)
draw_branches(start_point=tree.end_point, angle=0, length=100)
sd.pause()

