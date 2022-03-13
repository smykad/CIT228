import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from cannon_ball import CannonBall

class PirateFleet:
    
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.init()
        pygame.display.set_caption("Pirate Fleet")
        
        
        
        self.ship = Ship(self)
        self.cannon_balls = pygame.sprite.Group()
        
        
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for cannon_ball in self.cannon_balls.sprites():
            cannon_ball.draw_ball()
            
        pygame.display.flip()
    
    def _check_events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    sys.exit()
                case pygame.KEYDOWN:
                    self._check_keydown_events(event)
                case pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event): 
        match event.key:
            case pygame.K_DOWN:
                self.ship_fx('down')
            case pygame.K_UP:
                self.ship_fx('up')
            case pygame.K_q:
                sys.exit()
            case pygame.K_SPACE:
                self._fire_cannon()
                
                
    
    def _check_keyup_events(self, event):
        
        match event.key:    
            case pygame.K_DOWN:
                self.ship.moving_down = False
            case pygame.K_UP:
                self.ship.moving_up = False
    
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.cannon_balls.update()
            self._update_screen()
            
    def _fire_cannon(self):
        mySFX = pygame.mixer.Sound('pirate_fleet/media/shot.wav')
        new_cannon_ball = CannonBall(self)
        self.cannon_balls.add(new_cannon_ball)
        pygame.mixer.Sound.play(mySFX)
        
    def ship_fx(self, direction):
        mySFX = pygame.mixer.Sound('pirate_fleet/media/splash.wav')
        match direction:
            case 'up':
                self.ship.moving_up = True
            case 'down':
                self.ship.moving_down = True
        pygame.mixer.Sound.play(mySFX)
        
        
    
        
        
    
   
   
            
        

if __name__=='__main__':
    
    ai = PirateFleet()
    ai.run_game()
    
    