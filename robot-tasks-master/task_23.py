#!/usr/bin/python3

from pyrob.api import *

def task_6_6_old():
    is_Move = True
    move_up1 = True
    move_down1 = True
    move_right()
    while is_Move:
        while wall_is_above():    
            move_right()
        while move_up1 and not wall_is_on_the_right():
            
            move_up()
            fill_cell()
            move_up1 = not wall_is_above()
        while move_down1:
            move_down()
            move_down1 = not wall_is_beneath()
        
        is_Move = not wall_is_on_the_right()
        if is_Move == True:
            move_right()   
            move_up1 = True
            move_down1 = True
        else:
            is_Move == False
    while wall_is_beneath():
        move_left()





def Up_and_Down():
    fnMove1 = move_up
    move_up()
    while wall_is_on_the_left():
        if wall_is_above():
            fnMove1= move_down 
        fill_cell()
        fnMove1()
       

@task(delay=0.1)
def task_6_6():
    fnMove = move_right
    touch = False
    move_right()
    while wall_is_beneath():
        if not wall_is_above() and not touch:
            Up_and_Down()
        if wall_is_on_the_right():
            fnMove = move_left
            touch = True

        fnMove()

if __name__ == '__main__':
    run_tasks()
