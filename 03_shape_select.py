# -*- coding: utf-8 -*-

import simple_draw as sd

sd.set_screen_size(1200, 800)


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def triangle(x, y, angle, side):
    prev_point = sd.get_point(x, y)
    prev_angle = angle
    for _ in range(2):
        vector = sd.get_vector(start_point=prev_point, angle=prev_angle, length=side)
        vector.draw(width=5)
        prev_point = vector.end_point
        prev_angle += 120
    sd.line(start_point=prev_point, end_point=sd.get_point(x, y),width=5)


def square(x, y, angle, side):
    prev_point = sd.get_point(x, y)
    prev_angle = angle
    for _ in range(3):
        vector = sd.get_vector(start_point=prev_point, angle=prev_angle, length=side)
        vector.draw(width=5)
        prev_point = vector.end_point
        prev_angle += 90
    sd.line(start_point=prev_point, end_point=sd.get_point(x, y),width=5)


def pentagon(x, y, angle, side):
    prev_point = sd.get_point(x, y)
    prev_angle = angle
    for _ in range(4):
        vector = sd.get_vector(start_point=prev_point, angle=prev_angle, length=side)
        vector.draw(width=5)
        prev_point = vector.end_point
        prev_angle += 72
    sd.line(start_point=prev_point, end_point=sd.get_point(x, y),width=5)


def hexagon(x, y, angle, side):
    prev_point = sd.get_point(x, y)
    prev_angle = angle
    for _ in range(5):
        vector = sd.get_vector(start_point=prev_point, angle=prev_angle, length=side)
        vector.draw(width=5)
        prev_point = vector.end_point
        prev_angle += 60
    sd.line(start_point=prev_point, end_point=sd.get_point(x, y),width=5)

print('Choose the shape you want')
print('1)Triangle\n2)Square\n3)Pentagon\n4)Hexagon')

shape = int(input())
match shape:
    case 1:
        triangle(350, 100, 0, 600,)
    case 2:
        square(380, 100, 0, 500,)
    case 3:
        pentagon(400, 100, 0, 350,)
    case 4:
        hexagon(400, 100, 0, 350,)

sd.pause()
