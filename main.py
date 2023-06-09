import pygame
import sys
import os

class Cat:
    def __init__(self) -> None:
        self.speed = 5

        # Holds the image & object for Cat
        self.image = None
        self.object = None

        # Initial position of the cat is at the center of the arena
        self.posx = 520
        self.posy = 640

    def move(self):

        player_pos = pygame.Vector2(self.posx, self.posy)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 30 * self.speed
        if keys[pygame.K_s]:
            player_pos.y += 30 * self.speed
        if keys[pygame.K_a]:
            player_pos.x -= 30 * self.speed
        if keys[pygame.K_d]:
            player_pos.x += 30 * self.speed

class Dog:
    def __init__(self) -> None:
        self.speed = 3

        # Holds the image & object for Cat
        self.image = None
        self.object = None
        
        # Initial position of the cat is specified at the time of object creation
        self.posx = 0
        self.posy = 0

    def move(self, posx, posy):
        # Moves dog in a straight line and also change the path whenever it collides with the edges randomly
        player_pos = pygame.Vector2(posx, posy)

        pass





class Game:

    # Class Handling actual Game

    def __init__(self) -> None:
    
        pygame.init()

        SCREEN_WIDTH = 1280
        SCREEN_HEIGHT = 720

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill("white")

        clock = pygame.time.Clock()
        
        running = True

        speed = [1, 0]

        # Adding the animals in the game
        cat = Cat()
        cat.image = pygame.image.load('images/cat.png').convert()
        cat.object = cat.image.get_rect()
        cat.posx = (screen.get_size()[0]//2 - cat.image.get_size()[0])
        cat.posy = (screen.get_size()[1]//2 - cat.image.get_size()[1])

        dog1 = Dog()
        dog1.image = pygame.image.load('images/dog1.png').convert_alpha()
        dog1.object = dog1.image.get_rect()
        dog1.posx = 0
        dog1.posy = 0


        dog2 = Dog()
        dog2.image = pygame.image.load('images/dog2.png').convert_alpha()
        dog2.object = dog2.image.get_rect()
        dog2.posx = 0
        dog2.posy = SCREEN_HEIGHT-32

        dog3 = Dog()
        dog3.image = pygame.image.load('images/dog3.png').convert_alpha()
        dog3.object = dog3.image.get_rect()
        dog3.posx = SCREEN_WIDTH-32
        dog3.posy = 0


        dog4 = Dog()
        dog4.image = pygame.image.load('images/dog4.png').convert_alpha()
        dog4.object = dog4.image.get_rect()
        dog4.posx = SCREEN_HEIGHT-32  #Adjusting for the 32 pixels of the image
        dog4.posy = SCREEN_WIDTH-32


        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                """self.screen_size[0] / 2 - self.img.get_size()[0],
                self.screen_size[1] / 2 - self.img.get_size()[1]"""

                # Adding the cat in center
                screen.blit(cat.image, (cat.posx, cat.posy))
                # cat.move()

                # Adding dogs
                screen.blit(dog1.image, (dog1.posx, dog1.posy))

                screen.blit(dog2.image, (dog2.posx, dog2.posy))

                screen.blit(dog3.image, (dog3.posx, dog3.posy))

                screen.blit(dog4.image, (dog4.posx, dog4.posy))

            
            
            pygame.display.flip()




if __name__ == '__main__':
    Game()