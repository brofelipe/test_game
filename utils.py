import pygame
import cv2


class Sprite(object):
    def __init__(self, image_path, qtd_sprites, len_sprite = (100, 100), pos = (100, 100), heigher_jump = 20):
        self.spritesheet = pygame.image.load(image_path).convert()
        self.h, self.w, self.c = cv2.imread(image_path).shape
        self.qtd_sprites = qtd_sprites
        self.len_sprite = len_sprite
        self.aceleration_X = 0
        self.aceleration_Y = 1/5
        self.sprite_list = self.__get_sprites()
        self.sprite_rect = self.sprite_list[0].get_rect()
        self.current_frame = 0
        self.heigher_jump = heigher_jump
        self.pos_playerX, self.pos_playerY = pos
        self.ahead = True
        self.jumping = False
        self.falling = True

    def __get_sprites(self):
        sprite_list = []
        x = 0
        sprite_w = sprite_w_aux = self.w//self.qtd_sprites
        for i in range(self.qtd_sprites):
            sp = pygame.transform.scale(self.__get_sprite(x, 0, sprite_w - x, self.h), self.len_sprite)
            sprite_list.append(sp)
            x = sprite_w
            sprite_w += sprite_w_aux
        return sprite_list

    def __get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.spritesheet, (0, 0), (x, y, w, h))
        return sprite
    
    def current_sprite(self):
        if self.current_frame > 5 or self.current_frame < 0:
            self.current_frame = 0
        return self.sprite_list[int(self.current_frame)]
    
    def update(self, screen):
        self.pos_playerX += self.aceleration_X
        self.pos_playerY += self.aceleration_Y
        self.current_frame += abs(self.aceleration_X)/15
        self.sprite_rect.x, self.sprite_rect.y = self.pos_playerX, self.pos_playerY
        if self.ahead:
            sprite = self.current_sprite()
        else:
            sprite = pygame.transform.flip(self.current_sprite(), 180, 0)
        screen.blit(sprite, (self.pos_playerX, self.pos_playerY))
    
    def jump(self):
        self.aceleration_Y += -2
        if abs(self.aceleration_Y) >= self.heigher_jump:
            return False
        return True
    
    def collide(self, rect):
        if self.sprite_rect.colliderect(rect):
            return False
        return True
