import turtle


def draw_square(someturtle):
    
    for i   in  range(0,4):
        someturtle.forward(100)
        someturtle.right(90)

def draw_circle(angie):
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

 
def draw_art():
    window  =   turtle.Screen()
    window.bgcolor("red")
    
    
    brad    =   turtle.Turtle() #initialise function def init
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(0)
    for i   in  range(1,36):
        draw_square(brad)
        brad.right(10)

    #angie   =   turtle.Turtle()
    #draw_circle(angie)
    #window.exitonclick()

draw_art()
    
    
