import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from cannon_ball import CannonBall
from pirate import Pirate

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
        self.pirates = pygame.sprite.Group()
        
        self._create_fleet()
        
        
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for cannon_ball in self.cannon_balls.sprites():
            cannon_ball.draw_ball()
        
        self.pirates.draw(self.screen)      
            
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
            self._update_cannon()
            self._update_screen()
            
    def _fire_cannon(self):
        mySFX = pygame.mixer.Sound('pirate_fleet/media/shot.wav')
        if len(self.cannon_balls) < self.settings.cannon_balls_allowed:
            new_cannon_ball = CannonBall(self)
            self.cannon_balls.add(new_cannon_ball)
            pygame.mixer.Sound.play(mySFX)
    
    def _update_cannon(self):
        self.cannon_balls.update()
        screen_rect = self.screen.get_rect()
        for cannon_ball in self.cannon_balls.copy():
            if cannon_ball.rect.right >= screen_rect.right:
                self.cannon_balls.remove(cannon_ball)
        
    def ship_fx(self, direction):
        mySFX = pygame.mixer.Sound('pirate_fleet/media/splash.wav')
        match direction:
            case 'up':
                self.ship.moving_up = True
            case 'down':
                self.ship.moving_down = True
        pygame.mixer.Sound.play(mySFX)

    def _create_fleet(self):
        pirate = Pirate(self)
        
        pirate_height = pirate.rect.height
        pirate_width = pirate.rect.width
        available_space_x = self.settings.screen_width - (20 * pirate_width)
        number_pirates_x = available_space_x // (2 *pirate_width)

        available_space_y = self.settings.screen_height - (2 * pirate_height)
        number_rows = available_space_y // (2 *pirate_height)

        for row_number in range(number_rows):
            for pirate_number in range(number_pirates_x):
                # Create an alien and place it in the row. 
                self._create_pirate(pirate_number, row_number)
                
    def _create_pirate(self, pirate_number, row_number):
        """Create an alien and place it in the row"""
        pirate = Pirate(self)
        pirate_width, pirate_height = pirate.rect.size
        pirate.x = pirate_width + 2 * pirate_width * pirate_number
        pirate.rect.x = pirate.x
        pirate.rect.y = pirate.rect.height + 2 * pirate.rect.height * row_number
        self.pirates.add(pirate)
                
        

if __name__=='__main__':
    
    ai = PirateFleet()
    ai.run_game()
    
    