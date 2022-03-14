import pygame
import random
from pygame.sprite import Sprite


class Pirate(Sprite):
    
    def __init__(self, ai_game):
        
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        self.image = pygame.image.load('pirate_fleet/images/myPirate.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    """
    def update(self):
    
        self.x += (self.settings.pirate_speed * self.settings.fleet_direction)
        self.rect.x = self.x
        
    def check_edges(self):
    
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    """ 
        
 

