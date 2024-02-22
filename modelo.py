from random import randrange
from turtle import *
from freegames import square, vector

food = vector(0, 0)
robo = [vector(-240, 240)]
aim = vector(10, 0)
pontos = 0
blueBlocks = []
yellowBlocks = []
path = []

for i in range(25):
    blueBlocks.append(vector(randrange(-23, 23) * 10,randrange(-23, 23) * 10))

for i in range(25):
    yellowBlocks.append(vector(randrange(-23, 23) * 10,randrange(-23, 23) * 10))

def change(x, y):
    """Change robo direction."""
    aim.x = x
    aim.y = y

def addPonto(i):
    global pontos
    pontos +=i

def randDirection():
    rand = randrange(1,5)
    # print('rand:',rand)
    match rand:
        case  1:
            change(10, 0)    
        case  2:
            change(-10, 0)
        case  3:
            change(0, 10)
        case  4:
            change(0, -10)    

def mark(head):
    path.append(vector(head.x,head.y))
    
def scan(head):
    
    for i in blueBlocks:
        if head == i:
            
            addPonto(5)
            blueBlocks.remove(vector(head.x,head.y))
            print('Pontos:',pontos, '| Posição do Bloco: x',head.x,'y',head.y)
            return
            

    for i in yellowBlocks:
        if head == i:
            addPonto(10)
            yellowBlocks.remove(vector(head.x,head.y))
            print('Pontos:',pontos, '| Posição do Bloco: x',head.x,'y',head.y)
            return
    
    for i in path:
        if head == i:
            print('Ambiente já percorrido, sem Scan')
            return

    print('Scan : vazio')    
    mark(head)

def move():
    
    """Move robo forward one segment."""
    head = robo[-1].copy()
    randDirection()
    head.move(aim)
     
    if (head.y <= -240):
        change(0, 10)
        head.move(aim)
        update()
            
    
    if (head.y >= 230):
        change(0, -10)
        head.move(aim)
        update()

    if (head.x <= -240):
        change(10, 0)
        head.move(aim)
        update()

    if (head.x >= 230):
        change(-10, 0)
        head.move(aim)
        update()    
    
    robo.append(head)
    
    scan(head)

    robo.pop(0)

    clear()

    for i in blueBlocks:
        square(i.x,i.y,9,'blue')

    for i in yellowBlocks:
        square(i.x,i.y,9,'yellow')
    
    for i in path:
        square(i.x,i.y,9,'green')

    for body in robo:
        square(body.x, body.y, 9, 'black')

    update()
    ontimer(move, 10)


setup(520, 520, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()