from turtle import *


def draw_heart(scale=1, color_fill="red", color_outline="red"):
    pensize(3)
    color(color_outline, color_fill)  
    begin_fill()

    left(140)
    forward(180 * scale)
    circle(-90 * scale, 200)
    setheading(60)
    circle(-90 * scale, 200)
    forward(180 * scale)

    end_fill()


reset()
speed(3)
bgcolor("white")  
penup()
goto(0, -100)  
pendown()


draw_heart(scale=1, color_fill="red", color_outline="darkred")


penup()
goto(0, -60)  
setheading(0)
pendown()
draw_heart(scale=0.5, color_fill="white", color_outline="white")

penup()
goto(0, -250)
color("black")
write("Happy Mother's Day!", align="center", font=("Arial", 24, "bold"))

hideturtle()
mainloop()
