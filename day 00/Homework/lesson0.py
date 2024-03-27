from turtle import *

#We want to paint House/home

#We want Paint Wall for House 
begin_fill()
speed(30)
width(10)
color("blue")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of Wall

#We Want to Paint Door For House

forward(80)
color("brown")
begin_fill()
left(90)
forward(90)
right(90)
forward(50)
right(90)
forward(90)
end_fill()
#end of Door
#We want to paint roof
penup()
goto(200,200)
pendown()

color("gray")
begin_fill()
right(140)
forward(150)
left(98)
forward(150)
end_fill()
#end roof
#We want paint Windows
color("blue")
begin_fill()
left(41)
forward(50)
left(90)
color("cyan")
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
#left window
color("blue")
penup()
goto(200,200)
pendown()
begin_fill()

color("cyan")
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
exitonclick()