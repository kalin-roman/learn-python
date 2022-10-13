#!/usr/bin/python3

from operator import truediv
from pyrob.api import *


@task
def task_7_5():
    is_Move = True
    n = 0
    move_right()
    fill_cell()
    while is_Move:
        n += 1    
        for i in range(n):
            if  wall_is_on_the_right():                                 
                is_Move = False
                break
            move_right()
        if is_Move:
            fill_cell()
        
        


if __name__ == '__main__':
    run_tasks()
