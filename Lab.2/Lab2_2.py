"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


def QuadraticIsland(t, length):
    '''Draws a Quadratic island with length.'''
    if length < 10:         
        fd(t, length)
        return
    m = length / 3.0        # 控制迭代次数，3.0or6.0；6为一次迭代，3为二次迭代
    # 绘图迭代算法
    QuadraticIsland(t, m)
    lt(t, 90)
    QuadraticIsland(t, m)
    QuadraticIsland(t, m)
    rt(t, 90)
    QuadraticIsland(t, m)
    QuadraticIsland(t, m)
    rt(t, 90)
    QuadraticIsland(t, m)
    rt(t, 90)
    QuadraticIsland(t, m)
    lt(t, 90)
    QuadraticIsland(t, m)
    lt(t, 90)
    QuadraticIsland(t, m)
    QuadraticIsland(t, m)
    rt(t, 90)
    QuadraticIsland(t, m)
    rt(t, 90)
    QuadraticIsland(t, m)
    lt(t, 90)
    QuadraticIsland(t, m)
    lt(t, 90)
    QuadraticIsland(t, m)
    QuadraticIsland(t, m)
    lt(t, 90)
    QuadraticIsland(t, m)
    QuadraticIsland(t, m)
    rt(t, 90)
    QuadraticIsland(t, m)

def snowflake1(t, length, n, angle):
    '''Draws a Quadratic island with length.'''
    for i in range(n):                  # 控制绘图边数（三角形、正方形...）
        QuadraticIsland(t, length)
        rt(t, angle)                       # 度数依据于绘图边数，如三角形为120，正方形为90

def QuadraticType2Curve(t, length):
    '''Draws a QuadraticType2Curve with length.'''
    if length < 10:
        fd(t, length)
        return
    m = length / 3.0
    QuadraticType2Curve(t, m)
    lt(t, 90)
    QuadraticType2Curve(t, m)
    rt(t, 90)
    QuadraticType2Curve(t, m)
    rt(t, 90)
    QuadraticType2Curve(t, m)
    QuadraticType2Curve(t, m)
    lt(t, 90)
    QuadraticType2Curve(t, m)
    lt(t, 90)
    QuadraticType2Curve(t, m)
    rt(t, 90)
    QuadraticType2Curve(t, m)

def snowflake2(t, length):
    '''Draws a QuadraticType2Curve with length.'''
    for i in range(4):
        QuadraticType2Curve(t, length)
        rt(t, 90)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0

bob.x = -90
bob.y = 60
bob.redraw()

snowflake1(bob, 50, 1, 90)    # Quadratic island
# snowflake2(bob, 90)         # Quadratic type 2 curve
world.mainloop()
