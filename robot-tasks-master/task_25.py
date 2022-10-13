#!/usr/bin/python3

from pyrob.api import *

def cross():
    moves = [
        [move_up,move_down],
        [move_right, move_left],
        [move_down, move_up],
        [move_left,move_right]
    ]
    for action in moves:
        for fn in action:
            fill_cell()
            fn()

@task
def task_2_2():        
    move_right()
    move_down(2)
    for i in range(4):
        cross()
        move_right(4)
    cross()
    move_up()
    move_left()
if __name__ == '__main__':
    run_tasks()
