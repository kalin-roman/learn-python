#!/usr/bin/python3

from turtle import left
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
@task(delay=0.001)
def task_2_4():
    fnMove = move_right
    move_right()
    move_down()
    for g in range(5):
        if g % 2 == 0:
            fnMove =move_right
        else:
            fnMove = move_left
        for i in range(9):
            cross()
            fnMove(4)
        cross()
        if g != 4:
            move_down(4)
       
    move_left(37)
    move_up()
    


if __name__ == '__main__':
    run_tasks()
