#!/usr/bin/python3

from tkinter import wantobjects
from pyrob.api import *


@task
def task_5_10():
    is_Move = "right"

    while is_Move !="stop":
        if is_Move == "right":
            while not wall_is_on_the_right():
                fill_cell()
                move_right()
            is_Move = "left"

        elif is_Move  == "left":
            while not wall_is_on_the_left():
                fill_cell()
                move_left()
            is_Move = "right"
        if not wall_is_beneath():
            fill_cell()
            move_down()
        elif wall_is_on_the_left() and wall_is_beneath():
            is_Move ="stop"
        fill_cell()
if __name__ == '__main__':
    run_tasks()
