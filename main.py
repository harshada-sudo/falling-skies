import turtle
import random
import time
from tkinter import messagebox

delay=0.1
score =0
lives=3
#set the screen
wn=turtle.Screen()
wn.title("Falling skies")
wn.bgcolor("green")
wn.setup(width=800 , height= 600)
wn.tracer(0)

#create a pen
pen=turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()
pen.shape("square")
pen.color("white")
pen.goto(0,260)
pen.write("Score : {}   Lives : {}".format(score,lives),align="center",font=("times new area",20,"normal"))

#set a player
player=turtle.Turtle()
player.speed(0)
player.penup()
player.shape("square")
player.color("white")
player.goto(0,-260)
player.direction ="stop"

#create bad guys
good_guys=[]

for i in range(20):
    good_guy=turtle.Turtle()
    good_guy.speed(0)
    good_guy.penup()
    good_guy.shape("circle")
    good_guy.color("blue")
    good_guy.goto(-100,260)
    good_guy.speed = random.randint(1,4)
    good_guys.append(good_guy)

#create bad guys
bad_guys=[]

for i in range(20):
    #set good_guy
    bad_guy=turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.penup()
    bad_guy.shape("circle")
    bad_guy.color("red")
    bad_guy.goto(100,260)
    bad_guy.speed = random.randint(1,4)
    bad_guys.append(bad_guy)

#function
def go_left():
    player.direction = "left"

def go_right():    
    player.direction = "right"

#keyboard binding
wn.listen()
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")

#main game loop
while True:
    wn.update()

    #moving the player
    if player.direction == "left":
        x=player.xcor()
        player.setx(x-2)

    elif player.direction == "right":
        x=player.xcor()
        player.setx(x+2)   

    #moving the good guy
    for good_guy in good_guys:
        y=good_guy.ycor()
        good_guy.sety(y - good_guy.speed)
        
        #check if off the screen
        if y < -300:
            x = random.randint(-390,390)
            y= random.randint(300,400)
            good_guy.goto(x,y)

        #check for collision
        if good_guy.distance(player) < 20:
            x = random.randint(-390,390)
            y= random.randint(300,400)
            good_guy.goto(x,y)
            score +=10
            pen.clear()
            pen.write("Score : {}   Lives : {}".format(score,lives),align="center",font=("times new area",20,"normal"))

    #moving the bad guy
    for bad_guy in bad_guys:
        y=bad_guy.ycor()
        bad_guy.sety(y - bad_guy.speed)
        
        #check if off the screen
        if y < -300:
            x = random.randint(-390,390)
            y= random.randint(300,400)
            bad_guy.goto(x,y)

        #check for collision
        if bad_guy.distance(player) < 20:
            x = random.randint(-390,390)
            y= random.randint(300,400)
            bad_guy.goto(x,y)
            score -=10
            lives -=1

            if lives == 0:
                time.sleep(3)
                messagebox.showinfo("Game Status","Game Over !!!!.....Restarting again in 3 seconds")
                player.goto(0,-260)
                score = 0
                lives =3
            pen.clear()
            pen.write("Score : {}   Lives : {}".format(score,lives),align="center",font=("times new area",20,"normal"))
    
wn.mainloop()