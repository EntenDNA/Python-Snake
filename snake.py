import os
import pygame
import random as rd
pygame.init()

fgröse = 30
gröse = 30

class Snake():
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.body = []
        self.direction = (0,-1)

    def move(self):

        if self.direction == (0,-1):
            if self.y > 0:
               self.y += self.direction[1]

        elif self.direction == (0,1):
            if self.y < fgröse - 1:
               self.y += self.direction[1]

        elif self.direction == (1,0):
            if self.x < fgröse - 1:
               self.x += self.direction[0]

        elif self.direction == (-1,0):
            if self.x > 0:
               self.x += self.direction[0]

        self.body.append((self.x, self.y))


    def addpellet(self):
        self.body.append((self.x, self.y))

class Pellet():
    def __init__(self, x, y):

        self.x = x
        self.y = y

    def respawn(self):
        while True:
            self.x = rd.randint(0,fgröse-1)
            self.y = rd.randint(0,fgröse-1)

            if (self.x, self.y) not in snake.body:
                break
            else:
                continue

weis = (255,255,255)
schwarz = (0,0,0)
rot = (255,0,0)

width = fgröse * gröse
screen = pygame.display.set_mode((width, width))

clock = pygame.time.Clock()

snake = Snake(14,14)
pellet = Pellet(rd.randint(0,fgröse-1),rd.randint(0,fgröse-1))

gameover = False

while True:
    clock.tick(13)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            os._exit(1)

        elif event.type == pygame.KEYDOWN and not gameover:
            key = pygame.key.get_pressed()

            if key[pygame.K_LEFT] and snake.direction != (1,0):
                snake.direction = (-1,0)

            if key[pygame.K_RIGHT] and snake.direction != (-1,0):
                snake.direction = (1,0)

            if key[pygame.K_UP] and snake.direction != (0,1):
                snake.direction = (0,-1)

            if key[pygame.K_DOWN] and snake.direction != (0,-1):
                snake.direction = (0,1)


    if not gameover:
        screen.fill(schwarz)

        snake.move()

        if (snake.x, snake.y) in snake.body[:-1]:
            print("Your final length was:", len(snake.body))
            gameover = True

        if (snake.x, snake.y) == (pellet.x, pellet.y):
            pellet.respawn()
            snake.addpellet()

        for body in snake.body:
            bx, by = body
            pygame.draw.rect(screen, weis, (bx*gröse, by*gröse, gröse, gröse))

        snake.body.pop(0)

        pygame.draw.rect(screen, rot, (pellet.x*gröse, pellet.y*gröse, gröse, gröse))

        pygame.display.update()
