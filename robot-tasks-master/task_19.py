#!/usr/bin/python3

from turtle import left, right
from pyrob.api import *


@task
def task_8_29():
    # fnMove = move_right
    # right_wall = False
    # left_wall = False
    # while wall_is_above():
    #     if wall_is_on_the_right():
    #         fnMove = move_left
    #         left_wall = wall_is_on_the_left()
    #     elif wall_is_on_the_left():
    #         fnMove = move_right
    #         right_wall = wall_is_on_the_right()
    #     fnMove()
    #     print(right_wall,"",left_wall)
    # while not wall_is_above():
    #     move_up()
    # while not wall_is_on_the_left():
    #     move_left()
    is_Move = 1 #0 - stop, 1 - right, 2 - left, 3 - up
    wall_right = False
    wall_left = False
    while is_Move != 0:
        if not wall_is_above():# or wall_left and wall_right:
            is_Move = 0
        elif  wall_is_on_the_right():
            if  wall_right:
                is_Move = 0
            else:
                is_Move = 2
                wall_right = True
        elif wall_is_on_the_left():
            is_Move = 1
            wall_left = True 
        print(wall_right,"",wall_left)       
        if is_Move == 1:
            move_right()
        elif is_Move == 2:
            move_left()

            
    if not (wall_right and wall_left):
        while not wall_is_above():
            move_up()
        while not wall_is_on_the_left():
            move_left()



if __name__ == '__main__':
    run_tasks()
