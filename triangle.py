import turtle
import math
input = int(input("How big do you want it? "))
board = turtle.Turtle()
board.forward(input)
board.left(90)
board.forward(input)
board.left(135)
board.forward(math.hypot(input, input))
turtle.done()