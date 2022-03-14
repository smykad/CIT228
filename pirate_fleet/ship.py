import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    
    
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load('pirate_fleet/images/myShip.png')
        self.rect = self.image.get_rect()
        
        self.rect.midright = self.screen_rect.midright
        
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        
    def update(self):
        
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom: 
            self.y += 1
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1
        if self.moving_left and self.rect.left > 0:
            self.x -= 1
        self.rect.x = self.x
        
        self.rect.y = self.y
        
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
    
        