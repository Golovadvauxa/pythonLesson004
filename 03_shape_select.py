# -*- coding: utf-8 -*-

import simple_draw as sd

sd.set_screen_size(1200, 600)


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



shape = int(input())


sd.pause()
