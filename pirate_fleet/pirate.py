import pygame
from pygame.sprite import Sprite

class Pirate(Sprite):
    
    def __init__(self, ai_game):
        
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        self.image = pygame.image.load('pirate_fleet/images/pirate.png')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        
    def update(self):
        self.y += (self.settings.pirate_speed * self.settings.fleet_direction)
        self.rect.y = self.x
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.top or self.rect.bottom < self.screen_rect.bottom:
            return True