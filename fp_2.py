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

def draw_tree(order, size=100):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -window.window_height() // 3)
    t.pendown()
    t.left(90)  # Направляємо черепашку вертикально вгору

    draw_pythagoras_tree(t, order, size)

    window.mainloop()

# Отримуємо рівень рекурсії від користувача
try:
    user_input = int(input("Input a positive integer as recursion level for Pythagoras tree: "))
    if user_input < 0:
        raise ValueError("Recursion level cannot be negative.")
except ValueError as error:
    print(f"Error: {error}")
else:
    draw_tree(user_input)