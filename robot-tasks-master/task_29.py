#!/usr/bin/python3

from operator import truediv
from pyrob.api import *


@task
def task_7_7():
    is_Move = True
    n = 0
    while is_Move:
        if cell_is_filled():
            n += 1
        else:
            n = 0
        if n != 3 and not wall_is_on_the_right():
            move_right()
        else:
            is_Move = False
if __name__ == '__main__':
    run_tasks()
