# -*- coding: utf-8 -*-
import simple_draw as sd

sd.set_screen_size(1200, 600)


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

def triangle(x, y, angle, side, color):
    prev_point = sd.get_point(x, y)
    prev_angle = angle
    for _ in range(2):
        vector = sd.get_vector(start_point=prev_point, angle=prev_angle, length=side)
        vector.draw(color=color)
        prev_point = vector.end_point
        prev_angle += 120
    sd.line(start_point=prev_point, end_point=sd.get_point(x, y), color=color)


def square(x, y, angle, side, color):
    prev_point = sd.get_point(x, y)
    prev_angle = angle
    for _ in range(3):
        vector = sd.get_vector(start_point=prev_point, angle=prev_angle, length=side)
        vector.draw(color=color)
        prev_point = vector.end_point
        prev_angle += 90
    sd.line(start_point=prev_point, end_point=sd.get_point(x, y), color=color)


def pentagon(x, y, angle, side, color):
    prev_point = sd.get_point(x, y)
    prev_angle = angle
    for _ in range(4):
        vector = sd.get_vector(start_point=prev_point, angle=prev_angle, length=side)
        vector.draw(color=color)
        prev_point = vector.end_point
        prev_angle += 72
    sd.line(start_point=prev_point, end_point=sd.get_point(x, y), color=color)


def hexagon(x, y, angle, side, color):
    prev_point = sd.get_point(x, y)
    prev_angle = angle
    for _ in range(5):
        vector = sd.get_vector(start_point=prev_point, angle=prev_angle, length=side)
        vector.draw(color=color)
        prev_point = vector.end_point
        prev_angle += 60
    sd.line(start_point=prev_point, end_point=sd.get_point(x, y), color=color)


colors = {1: sd.COLOR_RED, 2: sd.COLOR_ORANGE, 3: sd.COLOR_YELLOW, 4: sd.COLOR_GREEN, 5: sd.COLOR_CYAN,
          6: sd.COLOR_BLUE, 7: sd.COLOR_PURPLE}
print('Choose the color of the shapes')
print('1)COLOR_RED\n'
      '2)COLOR_ORANGE\n'
      '3)COLOR_YELLOW\n'
      '4)COLOR_GREEN\n'
      '5)COLOR_CYAN\n'
      '6)COLOR_BLUE\n'
      '7)COLOR_PURPLE')
color_index = int(input())
color = colors[color_index]
triangle(100, 100, 0, 100, color)
square(250, 100, 0, 100, color)
pentagon(400, 100, 0, 80, color)
hexagon(580, 100, 0, 80, color)

sd.pause()
