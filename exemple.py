import pygame
import random
from utils import Sprite


hits = []
jumping = False
max_jump = 0
fps = 90
RESOLUTION = (1280, 720)

movement = {pygame.K_a:  (-fps/60,  0),
            pygame.K_d:  ( fps/60,  0)}

def main():
    global hits, jumping, max_jump
    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)
    screen_rect = screen.get_rect()
    clock = pygame.time.Clock()
    sprites = pygame.sprite.Group()
    blocks = pygame.sprite.Group()
    bg = pygame.image.load('sprites/game_background_4/game_background_4.png').convert()
    bg = pygame.transform.scale(bg, RESOLUTION)

    Sprite((640, 1075), pygame.Color('green'), blocks, tam=RESOLUTION)

    player = Sprite(screen_rect.center, path = 'sprites/cyborg/Cyborg_run.png')
    sprites.add(player)

    dt = 0
    while True:
        move = pygame.Vector2()
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE and not falling:
                    jumping = True

        pressed = pygame.key.get_pressed()
        for dir in (movement[key] for key in movement if pressed[key]):
            move += dir
        #if move.length() > 0: move.normalize_ip()

        print(len(hits))
        if 'bottom' not in hits:
            falling = True
        else:
            falling = False
            hits = []
        if falling and not jumping: move[1] = fps//50
        elif jumping: 
            move[1] = -fps/30
            max_jump += abs(move[1])
            if max_jump >= fps//3:
                max_jump = 0
                jumping = False

        player.pos += move * dt/(fps//30)

        screen.blit(bg, (0, 0))
        sprites.update()
        sprites.draw(screen)

        for block in pygame.sprite.spritecollide(player, blocks, False): # spritecollide e um metodo herdado de sprite
            clip = player.rect.clip(block.rect)
            hits = [edge for edge in ['bottom', 'top', 'left', 'right'] if getattr(clip, edge) == getattr(player.rect, edge)]

        pygame.display.flip()
        dt = clock.tick(fps)

if __name__ == '__main__':
    main()