import pygame
import sys
import sheet

pygame.init()

outerw, outerh = 900, 600
global innerh, innerw
innerw, innerh = 800, 470
white = (255,255,255)
black = (0,0,0)
bg = (48, 230, 136)
fps = 50


#screen creation
global screen
screen = pygame.display.set_mode((outerw,outerh))
pygame.display.set_caption("Conga Conga Conga!")

#Character sheet loading
global character
character = pygame.image.load('character_sheet.png').convert_alpha()
#Creating instance of sheet
ch_sheet = sheet.CharSheet(character)


def background():
    screen.fill(white)
    pygame.draw.rect(screen,bg,(50,60,innerw,innerh,))
    for i in range(4):
        pygame.draw.rect(screen,black,(50-i,60-i,innerw,innerh),1)
    
    global comicsans
    comicsans = pygame.font.Font('comicSans.ttf',32)
    text1 = comicsans.render('Conga, Conga, Conga!', True, black, white)
    text2 = comicsans.render('Followers : ', True, black, white)
    screen.blit(text1,(300,5))
    screen.blit(text2,(340,530))

    pygame.display.update()


x,y = 300,150

frame0 = ch_sheet.get_image1(80,73,2.5,black)
frame0_mask = pygame.mask.from_surface(frame0)
framefriend = ch_sheet.get_image2(80,173,2.5,black)
framefriend_mask = pygame.mask.from_surface(framefriend)
#mask_image = framefriend_mask.to_surface().convert_alpha()
friendposition = ch_sheet.random_posn(screen,framefriend)
frame0_rect = frame0.get_rect(center = (x,y))
framefriend_rect = framefriend.get_rect(center = (friendposition[0],friendposition[1]))


#open and quit
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(fps)

    background()

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        y-=5
    elif key[pygame.K_a]:
        x-=5
    elif key[pygame.K_s]:
        y+=5
    elif key[pygame.K_d]:
        x+=5
    elif key[pygame.K_q]:
        x-=3
        y-=3
    elif key[pygame.K_z]:
        x-=3
        y+=3
    elif key[pygame.K_e]:
        x+=3
        y-=3
    elif key[pygame.K_c]:
        x+=3
        y+=3
    
    if x <= 52:
        x = 62
    elif x >= 815:
        x = 805
    elif y <= 55:
        y = 55
    elif y >= 470:
        y = 470
    
    screen.blit(frame0,(x,y))
    #screen.blit(frame0_mask.to_surface(),(x,y))
    
    #Placing of friend in random spot
    screen.blit(framefriend,friendposition)
    #screen.blit(mask_image,(0,0))
    #olist = framefriend_mask.outline()
    #pygame.draw.polygon(screen,(200,150,150),olist,0)

    offsetx = frame0_rect.x - framefriend_rect.x
    offsety = frame0_rect.y - framefriend_rect.y

    #collisionchck = ch_sheet.collision(frame0,framefriend,frame0_rect,framefriend_rect)


    #print(collisionchck)
    #if collisionchck == 1:
    #    screen.blit(framefriend,ch_sheet.random_posn(screen,framefriend))
    #if frame0_mask.overlap(framefriend_mask,(offsetx,offsety)):
    #    print("1")
    #if frame0_rect.colliderect(framefriend_rect):
    #    print("1")
    

    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

