import pygame
from pygame.sprite import Sprite

class CannonBall(Sprite):
    
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.cannon_ball_color
        
        self.rect = pygame.Rect(0, 0, self.settings.cannon_ball_width, self.settings.cannon_ball_height)
        self.rect.midright = ai_game.ship.rect.midright
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def update(self):
        
        self.x += self.settings.cannon_ball_speed
        self.rect.x = self.x
        
        
    def draw_ball(self):
        
        pygame.draw.rect(self.screen, self.color, self.rect)
        

        

        