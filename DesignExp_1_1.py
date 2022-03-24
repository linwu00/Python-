# DesignExp_1_1.py

"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


def square(t, length):
    """Draws a square with sides of the given length.

    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        fd(t, length)
        lt(t)


def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360  # 运动的总距离
    n = int(arc_length / 4) + 1         # 运动的次数
    #n = int(arc_length)*4
    step_length = arc_length / n        # 步长
    step_angle = float(angle) / n       # 每一次转向的角度

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)


def circle(t, r):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    arc(t, r, 360)


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    world = TurtleWorld()      # 创建乌龟行动的环境

    bob = Turtle()              # 变量bob代表在TurtleWorld中的一只乌龟
    bob.delay = 0.001           # bob.delay代表每次行动之间的停顿，单位是秒。

    # draw a circle centered on the origin
    radius = 100                # 半径
    pu(bob)                     # 笔朝上，不会绘出轨迹
    fd(bob, radius)             # 乌龟的初始位置是在圆心的位置上，运动到半径上
    lt(bob)                     # 左转90
    pd(bob)                     # 笔朝下
    circle(bob, radius)         # 画圆
    wait_for_user()


    world2 = TurtleWorld()  # 画矩形
    bob2 = Turtle()
    bob2.delay = 0.1
    SQlen = 80
    square(bob2, SQlen)
    wait_for_user()
    
    world3 = TurtleWorld()  # 画正多边形
    bob3 = Turtle()
    bob3.delay = 0.1
    polen = 80
    polygon(bob3, 8, polen)
    wait_for_user()
