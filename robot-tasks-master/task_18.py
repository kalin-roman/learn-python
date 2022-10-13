#!/usr/bin/python3

from operator import truediv
from pyrob.api import *

@task
def task_8_28():
    fnMove = move_right
    while wall_is_above():
        if wall_is_on_the_right():
            fnMove = move_left
        elif wall_is_on_the_left():
            fnMove = move_right
        fnMove()
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()

def task_8_28_old1():
    is_Move = 1 #0 - stop, 1 - right, 2 - left, 3 - up
    while is_Move != 0:
        if not(wall_is_above()):
            is_Move = 0
        elif  wall_is_on_the_right():
            is_Move = 2
        elif wall_is_on_the_left():
            is_Move = 1
                        
        if is_Move == 1:
            move_right()
        elif is_Move == 2:
            move_left()
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()




def task_8_28_old():
    is_Move = 1 #0 - stop, 1 - right, 2 - left, 3 - up
    is_exit = False
    while is_Move != 0:
        if not(wall_is_above()):
            is_Move = 3
            is_exit = True
        elif  wall_is_on_the_right():
            is_Move = 2
        elif wall_is_on_the_left() and not(is_exit):
            is_Move = 1
                
        
        if is_Move == 1:
            move_right()
        elif is_Move == 2:
            move_left()
        elif is_Move == 3:
            if not (wall_is_above()):
                move_up()
            elif not(wall_is_on_the_left()):
                move_left()
            else:
                is_Move = 0


    


if __name__ == '__main__':
    run_tasks()
