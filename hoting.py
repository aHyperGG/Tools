import os
import random

def hotness():
    file = open('HOTNESS.txt', r)
    lines = file.enumerate()
    number = random.choice(0, lines)
    slash = print(readline(number))
    file.close()