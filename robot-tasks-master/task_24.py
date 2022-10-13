#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    moves = [
        [move_up,move_down],
        [move_right, move_left],
        [move_down, move_up],
        [move_left,move_right]
    ]
    move_right(2)
    move_down(2)
    for action in moves:
        for fn in action:
            fill_cell()
            fn()
    move_up()
    move_left()

def task_2_1_old():
    move_right(2)
    move_down(2)

    fill_cell()
    move_right()
    fill_cell()
    move_left()
    move_down()
    fill_cell()
    move_up()
    move_left()
    fill_cell()
    move_right()
    move_up()
    fill_cell()
    move_left()


if __name__ == '__main__':
    run_tasks()
