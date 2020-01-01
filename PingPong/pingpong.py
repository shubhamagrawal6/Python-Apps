#Learning python via projects
#PingPong game using turtle module

import turtle
import os


#Game ka screen
win = turtle.Screen()
win.title("PingPong by @shubhamagrawal6 :)")
win.bgcolor("black")
win.setup(width=800, height=600) #Defining size of the screen
win.tracer(0) #Stops window from updating so we can manually update it


#Score variables
sl = 0
sr = 0


#Left Paddle
pl = turtle.Turtle() #Creates a turtle object
pl.speed(0) #Speed of animation for paddle '0' being fastest
pl.shape("square")
pl.shapesize(stretch_wid = 5, stretch_len=1) #Stretches width of object by 5 times i.e. if width 20 changes to 100
#If only one of stretch_len or stretch_wid is set then both length and width are increased 
pl.color("white")
pl.penup() #Stops drawing when object is moving
pl.goto(-350, 0) #Sets initial position of the Paddle (every turtle starts at the center of the screen)


#Right Paddle
pr = turtle.Turtle() #Creates a turtle object
pr.speed(0) #Speed of animation for paddle '0' being fastest
pr.shape("square")
pr.shapesize(stretch_wid = 5, stretch_len=1) #Stretches width of object by 5 times i.e. if width 20 changes to 100
#If only one of stretch_len or stretch_wid is set then both length and width are increased 
pr.color("white")
pr.penup() #Stops drawing when object is moving
pr.goto(350, 0) #Sets initial position of the Paddle (every turtle starts at the center of the screen)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2 #This is the movement speed of ball set value according to system speed
ball.dy = 0.2


#Scoreboard
score = turtle.Turtle()
score.speed(0)
score.penup()
score.color("white")
score.hideturtle()
score. goto(0, 260)
score.write(f"Left: {sl}  Right: {sr}", align = "center", font=('helvetica', 20, 'normal'))


#Game chalane ke functions
def leftup():
    y = pl.ycor() #Gives y-coordinate of center of object
    if y >= 250:
        pl.sety(250)
    else:
        y += 25 #Move up by 25 pixels
        pl.sety(y) #Changing the y-coordinate

def rightup():
    y = pr.ycor() #Gives y-coordinate of center of object
    if y >= 250:
        pr.sety(250)
    else:
        y += 25 #Move up by 25 pixels
        pr.sety(y) #Changing the y-coordinate

def leftdown():
    y = pl.ycor() #Gives y-coordinate of center of object
    if y <= -250:
        pl.sety(-250)
    else:
        y -= 25 #Move down by 25 pixels
        pl.sety(y) #Changing the y-coordinate

def rightdown():
    y = pr.ycor() #Gives y-coordinate of center of object
    if y <= -250:
        pr.sety(-250)
    else:
        y -= 25 #Move down by 25 pixels
        pr.sety(y) #Changing the y-coordinate


#Keyboard se input
win.listen() #This tells the window to listen for inputs from keyboard
win.onkeypress(leftup, "w") #On pressing w it call function leftup
win.onkeypress(leftdown, "s")
win.onkeypress(rightup, "Up")
win.onkeypress(rightdown, "Down")



#Actual Game
while True:
    win.update()


    #Ball movement
    ball.setx(ball.xcor() + ball.dx) 
    ball.sety(ball.ycor() + ball.dy)


    #Border se Bounce
    if ball.ycor() >= 290:
        ball.sety(290) #Since movement is not round figure we need to reset position
        ball.dy *= -1
        os.system("aplay /home/shubham/Desktop/Pythongames/PingPong/bounce1.wav&") #For some reason had to give full path

    if ball.ycor() <= -290:
        ball.sety(-290) #Since movement is not round figure we need to reset position
        ball.dy *= -1
        os.system("aplay /home/shubham/Desktop/Pythongames/PingPong/bounce1.wav&")

    if ball.xcor() >= 390:
        ball.goto(0, 0)
        ball.dx *= -1
        sl += 1
        score.clear()
        score.write(f"Left: {sl}  Right: {sr}", align = "center", font=('helvetica', 20, 'normal'))
    
    if ball.xcor() <= -390:
        ball.goto(0, 0)
        ball.dx *= -1
        sr += 1
        score.clear()
        score.write(f"Left: {sl}  Right: {sr}", align = "center", font=('helvetica', 20, 'normal'))


    #Paddle se Bounce
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() > pr.ycor() - 40 and ball.ycor() < pr.ycor() + 40):
        ball.setx(340) #Since movement is not round figure we need to reset position
        ball.dx *= -1
        os.system("aplay /home/shubham/Desktop/Pythongames/PingPong/bounce2.wav&")

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() > pl.ycor() - 40 and ball.ycor() < pl.ycor() + 40):
        ball.setx(-340) #Since movement is not round figure we need to reset position
        ball.dx *= -1
        os.system("aplay /home/shubham/Desktop/Pythongames/PingPong/bounce2.wav&")
    

