from gamelib import *   

game=Game(800,750,"Ninja Tournament")
bk=Image("bamboo forest.jpg",game)
play = Image("play.png",game)
play.resizeBy(-40)
play.y +=89
game.setBackground(bk)

while not game.over:
    game.processInput()
    bk.draw()
    play.draw()
    
    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
  
    game.update(30)
