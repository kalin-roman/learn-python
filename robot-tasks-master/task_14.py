#!/usr/bin/python3

from pyrob.api import *

def up():
    move_up()
    fill_cell()
    move_down()
def down():
    move_down()
    fill_cell()
    move_up()
@task
def task_8_11():
    is_Move = True
    while is_Move:
        if not(wall_is_beneath()) and not(wall_is_above()):
            down()
            up()                
        elif not(wall_is_above()):
            up()
        elif not(wall_is_beneath()):
            down()
        else: 
            fill_cell()


        is_Move = not wall_is_on_the_right()
        if is_Move:
            move_right()
if __name__ == '__main__':
    run_tasks()
