# DesignExp_1_2.py

import turtle as t
t.color("red", "yellow")         # 画线颜色为红色，笔头颜色为黄色
t.speed(5)                  # 画线的速度
t.screensize(300, 300, bg="black")     # 设置屏幕大小，背景颜色为黑色
# 绘画
for i in range(100):            # 循环绘画
    t.fd(200)                   # forward，前进200像素
    t.left(170)                 # 左转170°
t.ht()               # 结束后隐藏笔头
t.exitonclick()         # 暂停绘图窗口
