import pygame
from utils import *

pygame.init()
clock = pygame.time.Clock()

# variables
BG = [70, 70, 200]

# screen 
screen_size = 800, 480
screen = pygame.display.set_mode(screen_size)
screen.fill(BG)
pygame.display.set_caption('Nome aq')

# player
player_sprite = Sprite('sprites/cyborg/Cyborg_run.png', 6)

# ground
rect_ground = (screen_size[0]//2 - 320, 288, 640, 900)

while True:
    if player_sprite.falling and not player_sprite.jumping: 
        player_sprite.aceleration_Y = 5
    elif player_sprite.jumping:
        player_sprite.jumping = player_sprite.jump()
    else: 
        player_sprite.aceleration_Y = 0
    
    # events
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and not player_sprite.falling:
                player_sprite.jumping = True
            if event.key == pygame.K_a:
                player_sprite.ahead = False
                player_sprite.aceleration_X = -3
            if event.key == pygame.K_d:
                player_sprite.ahead = True
                player_sprite.aceleration_X = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player_sprite.aceleration_X = 0
            if event.key == pygame.K_d:
                player_sprite.aceleration_X = 0

    # colisao com o chao
    player_sprite.falling = player_sprite.collide(rect_ground)

    # desenhando itens na tela
    screen.fill(BG)
    pygame.draw.rect(screen, (119, 255, 49), rect_ground) # chao kkkkkkk
    player_sprite.update(screen)
    pygame.display.update()
    clock.tick(90)

