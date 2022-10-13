#!/usr/bin/python3

from pyrob.api import *

def few_while():
    while not wall_is_beneath():
        move_down()
    while wall_is_beneath():
        move_right()
    move_down()
    while not wall_is_on_the_left():
        move_left()

def one_while():
    is_Move = True
    is_Wall = False
    is_end_wall = False
    to_Finish = False
    while is_Move:
        if not is_Wall:
            move_down()
            is_Wall = wall_is_beneath()
        elif not is_end_wall:
            move_right()
            is_end_wall = not wall_is_beneath()
        elif not to_Finish:
            move_down()
            to_Finish = True
        else:
            move_left()
            is_Move = not wall_is_on_the_left()

@task
def task_5_4():
    few_while()

if __name__ == '__main__':
    run_tasks()
