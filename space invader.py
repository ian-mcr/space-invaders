import pygame
WIDTH=800
HEIGHT=600
TITLE="space invaders"
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

shipOne=pygame.image.load("spaceship1.png")
shipTwo=pygame.image.load("spaceship2.png")
space=pygame.image.load("space3.png")


class Ship(pygame.sprite.Sprite):
    def __init__(self,x,y,image,angle):
        super().__init__()
        self.image=pygame.transform.scale(image,(70,70))
        self.image=pygame.transform.rotate(self.image,angle)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
ship1=Ship(250,250,shipOne,90)
ship2=Ship(500,250,shipTwo,-90)
sprites=pygame.sprite.Group()
sprites.add(ship1)
sprites.add(ship2)



run=True
while run:
    screen.blit(space,(0,0))
    pygame.draw.line(screen,"black",(400,0),(400,600),5)
    sprites.draw(screen)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_e:
                bullet=pygame.Rect(ship1.rect.x,ship1.rect.y)


    keyspressed=pygame.key.get_pressed()
    if keyspressed[pygame.K_w]:
        ship1.rect.y=ship1.rect.y-1
    if keyspressed[pygame.K_s]:
        ship1.rect.y=ship1.rect.y+1
    if keyspressed[pygame.K_a]:
        ship1.rect.x=ship1.rect.x-1    
    if keyspressed[pygame.K_d]:
        ship1.rect.x=ship1.rect.x+1
    if keyspressed[pygame.K_UP]:
        ship2.rect.y=ship2.rect.y-1
    if keyspressed[pygame.K_DOWN]:
        ship2.rect.y=ship2.rect.y+1
    if keyspressed[pygame.K_LEFT]:
        ship2.rect.x=ship2.rect.x-1
    if keyspressed[pygame.K_RIGHT]:
        ship2.rect.x=ship2.rect.x+1


























    pygame.display.update()       
             