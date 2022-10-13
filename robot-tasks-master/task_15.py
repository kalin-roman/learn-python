#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    n = 9 
    if wall_is_above() and wall_is_on_the_left():
        for i in range(n):
            move_right()
            move_down()
    elif wall_is_beneath() and wall_is_on_the_right():
        for f in range(n):
            move_left()
            move_up() 
    elif wall_is_on_the_left():
        for f in range(n):
            move_right()
            move_up() 
    else:
        for f in range(n):
            move_left()
            move_down()       


if __name__ == '__main__':
    run_tasks()
