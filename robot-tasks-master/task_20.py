#!/usr/bin/python3

from pyrob.api import *

def task_4_3_old():
    for f in range(6):
        for i in range(27):
            move_right()
            fill_cell()
        move_down()
        for p in range(27):
            fill_cell()
            move_left()
        move_down()    
    move_right()


@task(delay=0.05)
def task_4_3():
    for f in range(12):
        for j in range(27):
            if f % 2 == 0:
                move_right()  
                fill_cell()              
            else:
                fill_cell()
                move_left()        
        move_down()
    move_right()   
if __name__ == '__main__':
    run_tasks()
