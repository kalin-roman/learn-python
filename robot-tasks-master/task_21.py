#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():    
    for i in range(13):

        move_down()
        for h in range(i+1):
            move_right(1)
            fill_cell()
        move_left(i+1)

    move_down()
    move_right()
        


if __name__ == '__main__':
    run_tasks()
