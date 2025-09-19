"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector



snake_random_color = randrange(5)
food_random_color = randrange(5)
snake_color = ''
food_color = ''


food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

FOOD_DIRS = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def step_food():
    """Move food randomly one step without leaving the window."""
    candidates = []
    for d in FOOD_DIRS:
        nxt = p = food.copy()
        nxt.move(d)
        if inside(nxt):
            candidates.append(nxt)

    if candidates:
        nxt = choice(candidates)
        food.x, food.y = nxt.x, nxt.y



def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    step_food()

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)


if snake_random_color == 0:
    snake_color = 'blue'
elif snake_random_color == 1:
    snake_color = 'orange'
elif snake_random_color == 2:
    snake_color = 'green'
elif snake_random_color == 3:
    snake_color = 'purple'
else:
    snake_color = 'yellow'

if food_random_color == 0:
    food_color = 'blue'
elif food_random_color == 1:
    food_color = 'orange'
elif food_random_color == 2:
    food_color = 'green'
elif food_random_color == 3:
    food_color = 'purple'
else:
    food_color = 'yellow'



setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()
done()
