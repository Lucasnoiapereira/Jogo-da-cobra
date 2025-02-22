#!pip install pygame

import pygame
from pygame.locals import *
import random
import time

import pygame.locals

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

BLOCK = 10

pygame.font.init()
fonte = pygame.font.SysFont('arial', 35, True, True) 

def colision(pos1, pos2):
    return pos1 == pos2

def offLimit(pos):
    if 0 <= pos[0] < WINDOW_WIDTH and 0 <= pos[1] < WINDOW_HEIGHT:
            return False
    else:
        return True

def randomOnGrid(obstaculoPos):
     x = random.randint(0, WINDOW_WIDTH)
     y = random.randint(0, WINDOW_HEIGHT)
     if (x, y) in obstaculoPos:
          randomOnGrid
     return x // BLOCK * BLOCK, y // BLOCK * BLOCK

pontos = 0
velocidade = 10
pygame.init()
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Jogo da cobra')
snakePos = [(250, 50), (260, 50), (270, 50)]
snakeSurface = pygame.Surface((BLOCK, BLOCK))
snakeSurface.fill((53, 59, 72)) #353b48
snakeDirection = pygame.locals.K_LEFT

obstaculo_pos = []
obstaculo_surface = pygame.Surface((BLOCK, BLOCK))
obstaculo_surface.fill((0, 0, 0))


apple_surface = pygame.Surface((BLOCK, BLOCK))
apple_surface.fill((250, 0, 0))
apple_pos = randomOnGrid(obstaculo_pos)

def gameOver():
#   screen.fill((68, 189, 50)) #44bd32
    fonte = pygame.font.SysFont('Arial', 60, True, True)
    game_over = 'Game Over'
    texto_over = fonte.render(game_over, True, (255, 255, 255))
    window.blit(texto_over, (110, 300))
    pygame.display.update()
    time.sleep(5)
    pygame.quit()
while True:
    pygame.time.Clock().tick(velocidade)
    window.fill((68, 189, 50))
    mensagem = f'Pontos: {pontos}'
    texto = fonte.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.locals.KEYDOWN:
            if event.key in [pygame.locals.K_UP, pygame.locals.K_DOWN, pygame.locals.K_LEFT, pygame.locals.K_RIGHT]:
                if event.key == pygame.locals.K_DOWN and snakeDirection == pygame.locals.K_UP:
                    continue
                if event.key == pygame.locals.K_RIGHT and snakeDirection == pygame.locals.K_LEFT:
                    continue
                if event.key == pygame.locals.K_LEFT and snakeDirection == pygame.locals.K_RIGHT:
                    continue
                else:
                    snakeDirection = event.key 