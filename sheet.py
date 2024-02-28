import pygame
import random

class CharSheet():
    def __init__(self, image):
        self.sheet = image
    
    #Defining function inside CharSheet class
    def get_image1(self, width, height, scale, colour):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sheet,(-63,-50),(0,0,width,height))
        image = pygame.transform.scale(image,(width * scale, height * scale))
        image.set_colorkey(colour)
        self.mask = pygame.mask.from_surface(image)

        return image

    def get_image2(self, width, height, scale, colour):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sheet,(-63,-148),(0,0,width,height))
        image = pygame.transform.scale(image,(width * scale, height * scale))
        image.set_colorkey(colour)
        self.mask = pygame.mask.from_surface(image)

        return image
    
    def random_posn(self,screen,framefriend):
        global friendx,friendy
        friendx = random.randint(55,800)
        friendy = random.randint(65,470)

        return (friendx,friendy)
    
    def collision(self,frame0,framefriend,frame0_rect,framefriend_rect):
        pos = 0
        collide = pygame.sprite.collide_mask(frame0,framefriend)
        if collide != None:
            print("1")
        
        return pos
