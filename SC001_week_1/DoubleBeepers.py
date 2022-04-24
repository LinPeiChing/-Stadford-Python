"""
File: DoubleBeepers.py
Name:
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    move()
    double_beeper()
    move_back()
    go_home()


def double_beeper():
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_around()


def turn_around():
    turn_left()
    turn_left()


def move_back():
    move()
    # Karel is on beeper
    

def go_back():
    turn_around()
    move()












####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)