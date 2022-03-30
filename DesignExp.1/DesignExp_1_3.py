# 数字时钟

import turtle
from datetime import *

def Init():
    turtle.reset()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pensize(5)
    turtle.penup()
    turtle.left(180)
    turtle.forward(390)
    turtle.left(180)
       
def draw0():
    turtle.pendown()
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(160)
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)

def draw1():
    turtle.penup()
    turtle.forward(80)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(160)
    turtle.penup()
    turtle.left(180)
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(20)
    
def draw2():
    turtle.pendown()
    turtle.left(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.penup()
    turtle.forward(160)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(80)
    turtle.penup()
    turtle.forward(20)
    
def draw3():
    turtle.pendown()
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.penup()
    turtle.forward(80)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(80)
    turtle.penup()
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(80)
    turtle.left(90)
    
def draw4():
    turtle.penup()
    turtle.forward(80)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(160)
    turtle.left(90)
    turtle.penup()
    turtle.forward(80)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(80)
    turtle.penup()
    turtle.left(90)
    turtle.forward(20)
    
def draw5():
    turtle.pendown()
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(80)
    turtle.penup()
    turtle.right(90)
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(20)
    
def draw6():
    turtle.pendown()
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(80)
    turtle.backward(160)
    turtle.left(90)
    turtle.forward(80)
    turtle.penup()
    turtle.right(90)
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(20)
    
def draw7():
    turtle.penup()
    turtle.left(90)
    turtle.forward(160)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(160)
    turtle.penup()
    turtle.left(90)
    turtle.forward(20)

def draw8():
    turtle.pendown()
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(160)
    turtle.backward(80)
    turtle.left(90)
    turtle.forward(80)
    turtle.penup()
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(80)
    turtle.left(90)
    
def draw9():
    turtle.pendown()
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(80)
    turtle.penup()
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(80)
    turtle.left(90)
    
def drawm():
    turtle.pendown()
    turtle.forward(80)
    turtle.penup()
    turtle.forward(20)
    
def drawNum(a):
    if a == 0:
        draw0()
    elif a == 1 :
        draw1()
    elif a == 2 :
        draw2()
    elif a == 3 :
        draw3()
    elif a == 4 :
        draw4()
    elif a == 5 :
        draw5()
    elif a == 6 :
        draw6()
    elif a == 7 :
        draw7()
    elif a == 8 :
        draw8()
    elif a == 9 :
        draw9()

def Tick():
    #Init()
    turtle.clear()
    turtle.tracer(False)
    t = datetime.today()
    second = t.second
    minute = t.minute
    hour = t.hour
    a = hour//10
    drawNum(a)
    a = hour%10
    drawNum(a)
    drawm()    
    a = minute//10
    drawNum(a)
    a = minute%10
    drawNum(a)
    drawm()  
    a = second//10
    drawNum(a)
    a = second%10
    drawNum(a)
    turtle.penup()
    turtle.backward(800)
    turtle.tracer(True)
    turtle.ontimer(Tick, 1000)
    
def main():
    turtle.tracer(False)
    Init()
    turtle.tracer(True)
    Tick()
    turtle.mainloop()
    
if __name__ == "__main__":
    main()
