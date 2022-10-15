import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, player_name, key_map, player_color, SCREEN_WIDTH, SCREEN_HEIGHT):
        super(Player, self).__init__()
        self.name = player_name
        self.surf = pygame.Surface((25,25))
        self.surf.fill(player_color)
        self.key_map = key_map
        self.screen_size = [SCREEN_WIDTH,SCREEN_HEIGHT]
        self.rect = self.surf.get_rect()

    def move_player(self, pressed_keys):
        if pressed_keys[self.key_map[0]]:
            self.rect.move_ip(0, -5)
            if self.rect.top <= 0:
                self.rect.top = 0
        if pressed_keys[self.key_map[1]]:
            self.rect.move_ip(0, 5)
            if self.rect.bottom >= self.screen_size[1]:
                self.rect.bottom = self.screen_size[1]
        if pressed_keys[self.key_map[2]]:
            self.rect.move_ip(-5, 0)
            if self.rect.left < 0:
                self.rect.left = 0
        if pressed_keys[self.key_map[3]]:
            self.rect.move_ip(5, 0)
            if self.rect.right > self.screen_size[0]:
                self.rect.right = self.screen_size[0]