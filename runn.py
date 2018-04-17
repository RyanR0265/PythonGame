
from gamelib import *

game=Game(800,750,"Character Movement")
bk=Image("Dojo_Background.JPG",game)
bk.resizeTo(800,750)
game.setBackground(bk)
stars=Image("Ninja_star.PNG",game)
stars2=Image("Ninja_star2.PNG",game)
stars3=Image("Ninja_star3.PNG",game)
stars4=Image("Ninja_star4.PNG",game)
stars5=Image("Ninja_star5.PNG",game)
stars6=Image("Ninja_star6.PNG",game)
stars7=Image("Ninja_star7.PNG",game)
stars8=Image("Ninja_star8.PNG",game)
sword = Image("weapon1.png",game)
sword2 = Image("weapon2.png",game)
sword3 = Image("weapon3.png",game)
sword4 = Image("weapon4.png",game)


#Graphics
smurf = Animation("MOVES2.png",5,game,356/3,377/3,2)
sword = Image("weapon1.png",game)

bar=Animation("bar.png",3,game,2100/3,110)
bar.moveTo(bar.x,game.height)
sword.moveTo(250,600)
sword.resizeBy(-50)
smurf.moveTo(bar.x,bar.y-100)
sword.moveTo(350,600)
sword2.moveTo(610,435)
sword3.moveTo(220,520)
sword4.moveTo(400,430)
sword2.resizeBy(-50)
sword3.resizeBy(-50)
sword4.resizeBy(-50)


a=randint(2,110)
b=randint(2,110)
c=randint(2,110)
d=randint(2,110)
e=randint(2,110)
f=randint(2,110)
g=randint(2,110)
h=randint(2,110)

stars.resizeBy(-95)
stars.moveTo(700,500)
stars.setSpeed(10,40)

stars2.resizeBy(-95)
stars2.moveTo(283,a)
stars2.setSpeed(10,382)

stars3.resizeBy(-95)
stars3.moveTo(291,g)
stars3.setSpeed(10,710)

stars4.resizeBy(-95)
stars4.moveTo(a,a)
stars4.setSpeed(10,459)

stars5.resizeBy(-95)
stars5.moveTo(a,a)
stars5.setSpeed(10,504)

stars6.resizeBy(-95)
stars6.moveTo(a,a)
stars6.setSpeed(10,210)

stars7.resizeBy(-95)
stars7.moveTo(a,a)
stars7.setSpeed(10,239)

stars8.resizeBy(-95)
stars8.moveTo(a,a)
stars8.setSpeed(10,300)


jumping = False
factor = 1
landed = False
collected=0
                    
#Sound

#Level 1
while not game.over:
    game.processInput()
    bk.draw()
    smurf.draw()
    sword.draw()
    sword.draw()
    sword2.draw()
    sword3.draw()
    sword4.draw()

    smurf.stop()#stops animating (displays last frame)
    if keys.Pressed[K_RIGHT]:
        smurf.nextFrame() #advances one frame at a time
        smurf.x +=5 #moves to right
    if keys.Pressed[K_LEFT]:
        smurf.prevFrame() # retreats one frame at a time
        smurf.x -=5 #moves to left
    if smurf.collidedWith(bar) and smurf.y>=game.height-50:
        smurf.y+=0
    if smurf.collidedWith(sword):
        sword.visible=False
        
    stars.move(True)
    stars2.move(True)
    stars3.move(True)
    stars4.move(True)
    stars5.move(True)
    stars6.move(True)
    stars7.move(True)      
    stars8.move(True)
        

    if smurf.collidedWith(sword):
        sword.visible=False
        collected+=1
        

    if smurf.collidedWith(sword2):
        sword2.visible=False
        collected+=1

    if smurf.collidedWith(sword3):
        sword2.visible=False
        collected+=1

    if smurf.collidedWith(sword4):
        sword3.visible=False
        collected+=1

    if smurf.collidedWith(stars):
        smurf.health-=20
        stars.visible=False

    if smurf.collidedWith(stars2):
        smurf.health-=20
        stars2.visible=False

    if smurf.collidedWith(stars3):
        smurf.health-=20
        stars3.visible=False

    if smurf.collidedWith(stars4):
        smurf.health-=20
        stars4.visible=False

    if smurf.collidedWith(stars5):
        smurf.health-=20
        stars5.visible=False

    if smurf.collidedWith(stars6):
        smurf.health-=20
        stars6.visible=False

    if smurf.collidedWith(stars7):
        smurf.health-=20
        stars7.visible=False

    if smurf.collidedWith(stars8):
        smurf.health-=20
        stars8.visible=False

    if smurf.health<=0:
        game.over=True

    if collected>=4:
        game.over=True

    game.drawText("Health: " + str(smurf.health),smurf.x - 20,smurf.y + 50)
    game.drawText("Sword collected: " + str(smurf.health),smurf.x - 20,smurf.y + 50)
        

        


    #while jumping:
        #smurf[index].append(Animation("jump.png",2,game,238/2,124,3))
    
    if jumping:
        smurf.y -= 31 * factor 
        factor *= .95
        landed = False
    if factor < .31:
        jumping = False
        factor = 1
    if keys.Pressed[K_SPACE] and smurf.collidedWith(bar) and not jumping:
        jumping = True
    if not smurf.collidedWith(bar,"rectangle"):
        smurf.y += 12

game.over=False

game.update(60)



