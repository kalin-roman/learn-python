#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_4():
    is_Move = True
    while is_Move:
        if wall_is_above() and wall_is_beneath():
            fill_cell()
        is_Move = not wall_is_on_the_right()
        if is_Move:
            move_right()



if __name__ == '__main__':
    run_tasks()
