import pgzrun
#add bgm music
music.play('bg')
b = Rect((30,50),(30,50))
vx = 3      #global variable
vy = 5

def draw():
    screen.fill('black')
    #screen.draw.filled_rect(b,'yellow')

def update():
    global vx,vy
    b.x += vx
    b.y += vy
    if b.right > 800 or b.left < 0:
        vx = -vx
        sounds.s1.play()
    
    if b.bottom >600 or b.top <0:
        vy = -vy
        sounds.s1.play()
        
        

# outside of all function
pgzrun.go()
