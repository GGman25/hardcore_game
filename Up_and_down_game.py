import turtle
import time
import random

def draw_borders(bottom,top):
    helper.clear()
    helper.setpos(2000,bottom)
    helper.down()
    helper.setpos(-2000,bottom)
    helper.up()
    helper.setpos(2000,top)
    helper.down()
    helper.setpos(-2000,top)
    helper.up()

def reverse_gravity(x,y):
    global GRAVITY
    GRAVITY = GRAVITY * -1

w = turtle.Screen()
w.tracer(0)
w.title("Up and down game")

helper = turtle.Turtle()
helper.speed(0)
helper.up()
helper.ht()

t = turtle.Turtle()
t.shape('triangle')
t.shapesize(1)
t.up()
t.speed(0)
t.dy = 0
t.width = 3
t.height = 6

GRAVITY = -10
BOTTOM = -300
TOP = 300
CAN_PLAY = True

draw_borders(BOTTOM,TOP)
w.onclick(reverse_gravity)
while True:
    if CAN_PLAY:
        if BOTTOM < -35 and TOP > 35:
            if t.dy > BOTTOM and t.dy < TOP:
                t.dy -= GRAVITY
                t.sety(t.dy)
                time.sleep(0.03)
                BOTTOM += 1
                TOP -= 1
                draw_borders(BOTTOM,TOP)
                w.update()
            else:
                helper.setpos(0,TOP+10)
                helper.write('You lose')
                CAN_PLAY = False
                break
        else:
            helper.setpos(0,TOP+20)
            helper.write('You win')
            CAN_PLAY = False
            break
    pass

w.mainloop()