# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg
sd.set_screen_size(1200, 600)


# def triangle(x, y, angle, side):
#     point = sd.get_point(x, y)
#     v1 = sd.get_vector(start_point=point, angle=angle, length=side)
#     v1.draw(width=3)
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=side)
#     v2.draw(width=3)
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=side)
#     v3.draw(width=3)
#
#
# def square(x, y, angle, side):
#     point = sd.get_point(x, y)
#     v1 = sd.get_vector(start_point=point, angle=angle, length=side)
#     v1.draw(width=3)
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=side)
#     v2.draw(width=3)
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=side)
#     v3.draw(width=3)
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=side)
#     v4.draw(width=3)
#
#
# def pentagon(x, y, angle, side):
#     point = sd.get_point(x, y)
#     v1 = sd.get_vector(start_point=point, angle=angle, length=side)
#     v1.draw(width=3)
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=side)
#     v2.draw(width=3)
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=side)
#     v3.draw(width=3)
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=side)
#     v4.draw(width=3)
#
#     sd.line(start_point=v4.end_point, end_point=point, width=3)
#
#
# def hexagon(x, y, angle, side):
#     point = sd.get_point(x, y)
#     v1 = sd.get_vector(start_point=point, angle=angle, length=side)
#     v1.draw(width=3)
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=side)
#     v2.draw(width=3)
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=side)
#     v3.draw(width=3)
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=side)
#     v4.draw(width=3)
#
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=side)
#     v5.draw(width=3)
#
#     sd.line(start_point=v5.end_point,end_point=point,width=3)
#
#
# triangle(x=100, y=100, angle=0, side=200)
# square(x=350, y=100, angle=0, side=150)
# pentagon(x=550, y=100, angle=0, side=100)
# hexagon(x=750, y=100, angle=0, side=100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?
def triangle(x, y, angle, side):
    prev_point = sd.get_point(x, y)
    prev_angle = angle
    for _ in range(2):
        vector = sd.get_vector(start_point=prev_point, angle=prev_angle, length=side)
        vector.draw()
        prev_point = vector.end_point
        prev_angle += 120
    sd.line(start_point=prev_point, end_point=sd.get_point(x, y))


def square(x, y, angle, side):
    prev_point = sd.get_point(x, y)
    prev_angle = angle
    for _ in range(3):
        vector = sd.get_vector(start_point=prev_point, angle=prev_angle, length=side)
        vector.draw()
        prev_point = vector.end_point
        prev_angle += 90
    sd.line(start_point=prev_point, end_point=sd.get_point(x, y))


def pentagon(x, y, angle, side):
    prev_point = sd.get_point(x, y)
    prev_angle = angle
    for _ in range(4):
        vector = sd.get_vector(start_point=prev_point, angle=prev_angle, length=side)
        vector.draw()
        prev_point = vector.end_point
        prev_angle += 72
    sd.line(start_point=prev_point, end_point=sd.get_point(x, y))


def hexagon(x, y, angle, side):
    prev_point = sd.get_point(x, y)
    prev_angle = angle
    for _ in range(5):
        vector = sd.get_vector(start_point=prev_point, angle=prev_angle, length=side)
        vector.draw()
        prev_point = vector.end_point
        prev_angle += 60
    sd.line(start_point=prev_point, end_point=sd.get_point(x, y))


triangle(100, 100, 0, 100)
square(250, 100, 0, 100)
pentagon(400, 100, 0, 80)
hexagon(580, 100, 0, 80)
# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
