#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_9_3():
    i = 1 
    fnMove = move_right
    fnWall = wall_is_on_the_right
    while i <= 5:
        if i % 2 == 0:
            fnMove = move_left
            fnWall = wall_is_on_the_left
        else:
            fnMove = move_right
            fnWall = wall_is_on_the_right
        j = 1
        is_Move = True
        while is_Move:
            max, min = i, j
            if max < j:
                max, min = j, i
            if max % min > 0 or (i == 1 and j > 1 and not wall_is_on_the_right()) or (j == 1 and i > 1 and not wall_is_on_the_left()):
                fill_cell()
            if fnWall():
                is_Move = False
            else:
                fnMove()    
            j += 1
        i += 1
        if not wall_is_beneath():
            move_down()
    
if __name__ == '__main__':
    run_tasks()
