from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_position = [(0,0), (-20,0), (-40,0)]
for i in starting_position:
    segment = Turtle("square")
    segment.color("white")
    segment.goto(i)

screen.exitonclick()