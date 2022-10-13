#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    is_Move = True
    n = 0
    while is_Move:
        if cell_is_filled():
            n +=1        
        if n != 5:
            move_right()
        else:
            is_Move = False

if __name__ == '__main__':
    run_tasks()
