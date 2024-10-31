import turtle
import math


def draw_pythagoras_tree(t, order, size, angle=45):
    if order == 0:
        t.forward(size)
        t.backward(size)
    else:
        t.forward(size)
        pos = t.position()
        heading = t.heading()

        # Ліва гілка
        t.left(angle)
        draw_pythagoras_tree(t, order - 1, size * math.sqrt(2) / 2, angle)
        
        # Повертаємося до стовбура
        t.setposition(pos)
        t.setheading(heading)
        
        # Права гілка
        t.right(angle)
        draw_pythagoras_tree(t, order - 1, size * math.sqrt(2) / 2, angle)
        
        # Повертаємося до вихідної позиції
        t.setposition(pos)
        t.setheading(heading)

