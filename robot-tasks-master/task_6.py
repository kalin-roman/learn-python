#!/usr/bin/python3

from tkinter.tix import Tree
from pyrob.api import *


@task
def task_5_3():
    is_move = True
    is_prev_wall = False
    while is_move :
        move_right()
        isWallUnder = wall_is_beneath()
        is_move = not(is_prev_wall) or isWallUnder
        is_prev_wall = isWallUnder

            


if __name__ == '__main__':
    run_tasks()
