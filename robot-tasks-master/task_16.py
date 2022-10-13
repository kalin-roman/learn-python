#!/usr/bin/python3

from bisect import insort_left
from pyrob.api import *
def father():
    is_Move = True
    is_Left = False
    is_Right = False
    is_Wall = False
    while is_Move:        
        if not is_Wall:
            move_up()
            is_Wall = wall_is_above()
        elif not is_Left and not is_Right:
            is_Left = not wall_is_on_the_left()
            is_Right = not wall_is_on_the_right()
        elif is_Left:
            move_left()
            is_Move =not wall_is_on_the_left()
        elif is_Right:
            move_right()
            is_Move = not wall_is_on_the_right()

@task
def task_8_22():
    while not wall_is_above():
        move_up()
    if not wall_is_on_the_left():
        while not wall_is_on_the_left():
            move_left()
    else:
        while not wall_is_on_the_right():
            move_right()

        
         


if __name__ == '__main__':
    run_tasks()
