TITLE = 'Flappy Bird'
WIDTH = 400
HEIGHT = 708



def update():
    bird.speed += gravity
    bird.y += bird.speed
    top_pipe.x -= scroll_speed
    bottom_pipe.x -= scroll_speed
    if top_pipe.right < 0:
        top_pipe.left = WIDTH
        bottom_pipe.left = WIDTH
    if bird.y > HEIGHT:
        reset()
    if (bird.colliderect(top_pipe) or bird.colliderect(bottom_pipe)):
        hit_pipe()


def on_mouse_down():
    if (bird.alive):
        bird.speed = -6.5

def on_key_down(key):
    global godmode
    if (bird.alive):
        if (key == keys.SPACE):
            bird.speed = -6.5
        if (key == keys.C):
            if godmode == True:
                godmode = False
                print('Godmode: OFF')
            else:
                godmode = True
                print('Godmode: ON')
            

def reset():
    print ("Back to the start...")
    bird.speed = 1
    bird.center = (75, 75)
    top_pipe.center = (300, 0)
    bottom_pipe.center = (300, top_pipe.height + gap)
    bird.image = 'bird1'
    bird.alive = True
    
    
def hit_pipe():
    if godmode == False:
        print ("Hit pipe!")
        bird.image = "birddead"
        bird.alive = False
    



def draw():
    screen.blit('cascade', (0, 0))
    bird.draw()
    top_pipe.draw()
    bottom_pipe.draw()

bird = Actor('bird1', (75, 350))


godmode = False
gap = 140
top_pipe = Actor('top', (300, 0))
bottom_pipe = Actor('bottom', (300, top_pipe.height + gap))

scroll_speed = 3
gravity = 0.3

reset()