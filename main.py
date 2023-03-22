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
        self.posx = 640
        self.posy = 520

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

        screen = pygame.display.set_mode((1280, 720))
        screen.fill("white")

        clock = pygame.time.Clock()
        
        running = True

        speed = [1, 0]

        # Adding the animals in the game
        cat = Cat()
        cat.image = pygame.image.load('images/cat.png').convert()
        cat.object = cat.image.get_rect()

        dog1 = Dog()
        dog1.image = pygame.image.load('images/dog1.png').convert()
        dog1.object = dog1.image.get_rect()
        dog1.posx = 0


        dog2 = Dog()
        dog2.image = pygame.image.load('images/dog2.png').convert()
        dog2.object = dog2.image.get_rect()

        dog3 = Dog()
        dog3.image = pygame.image.load('images/dog3.png').convert()
        dog3.object = dog3.image.get_rect()

        dog4 = Dog()
        dog4.image = pygame.image.load('images/dog4.png').convert()
        dog4.object = dog4.image.get_rect()


        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            """Problem 2: Make a more random movement pattern"""
            cat.move()

            # blit() copies the pixels from one object to another surface
            """Problem 1: Remove the black trail left behind by the image"""
            screen.blit(cat.image, cat.object, special_flags=0)
            
            
            pygame.display.flip()




if __name__ == '__main__':
    Game()