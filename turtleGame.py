import turtle as t
import random

speed=9.5
score=0
good=0

def play():
    global score
    global speed
    t.forward(10)
    te.setheading(te.towards(t.pos()))
    te.forward(speed)

    if t.distance(tf.pos())<=12:
        x=random.randint(-230,230)
        y=random.randint(-230,230)
        x1=random.randint(-230,230)
        y1=random.randint(-230,230)
        tf.goto(x,y)
        te.goto(x1,y1)
        t.write(str(score),False,"center",("",20))
        score=score+1
        
    if t.distance(te.pos())>=12:
        t.ontimer(play,100)
    
    if t.distance(te.pos())<12:
        t.clearscreen()
        t.write("GameOver",False,"center",("",20))

def start():
        t.clear()
        play()
        
def up():
    t.setheading(90)

def down():
    t.setheading(270)

def right():
    t.setheading(0)

def left():
    t.setheading(180)


t.shape("turtle")
t.setup(500,500)
t.bgcolor("orange")
t.up()
t.speed(0)
t.goto(0,100)
t.write("거북이팩맨",False,"center",("",20))
t.goto(0,-100)
t.write("시작:Space",False,"center",("",15))
t.goto(0,0)
t.color("white")

t.onkeypress(up,"Up")
t.onkeypress(down,"Down")
t.onkeypress(right,"Right")
t.onkeypress(left,"Left")
t.onkeypress(start,"space")
t.listen()

te=t.Turtle()
te.shape("turtle")
te.color("red")
te.up()
te.speed(0)
te.goto(0,200)


tf=t.Turtle()
tf.shape("circle")
tf.color("green")
tf.up()
tf.speed(0)
tf.shapesize(0.5)
tf.goto(0,-200)
