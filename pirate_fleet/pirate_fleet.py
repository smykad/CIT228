import sys
from time import sleep
import random

import pygame

from settings import Settings
from ship import Ship
from cannon_ball import CannonBall
from pirate import Pirate
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard

class PirateFleet:
    
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.screen_rect = self.screen.get_rect()
        pygame.init()
        pygame.display.set_caption("Pirate Fleet")
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        
        self.ship = Ship(self)
        self.cannon_balls = pygame.sprite.Group()
        self.pirates = pygame.sprite.Group()
        self._create_fleet()
        
        self.play_button = Button(self, "Play")
        
        
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for cannon_ball in self.cannon_balls.sprites():
            cannon_ball.draw_ball()
        
        self.pirates.draw(self.screen)
        self.sb.show_score()
        
        if not self.stats.game_active:
            self.play_button.draw_button()   
            
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
                case pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event): 
        match event.key:
            case pygame.K_DOWN:
                self.ship_fx('down')
            case pygame.K_UP:
                self.ship_fx('up')
            case pygame.K_LEFT:
                self.ship_fx('left')
            case pygame.K_RIGHT:
                self.ship_fx('right')
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
            case pygame.K_LEFT:
                self.ship.moving_left = False
            case pygame.K_RIGHT:
                self.ship.moving_right = False
                
    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_ships()
            
            self.pirates.empty()
            self.cannon_balls.empty()
            
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)
    
    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_cannon()
                self._update_pirates()
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
            if cannon_ball.rect.left < screen_rect.left:
                self.cannon_balls.remove(cannon_ball)
        self._check_cannon_pirate_collisions()
    
    def _check_cannon_pirate_collisions(self):
        mySFX = pygame.mixer.Sound('pirate_fleet/media/piratesink.wav')
        collisions = pygame.sprite.groupcollide(self.cannon_balls, self.pirates, True, True)
        if collisions:
            for pirates in collisions.values():
                self.stats.score += self.settings.pirate_points * len(pirates)    
            self.sb.prep_score()
            pygame.mixer.Sound.play(mySFX)
        if not self.pirates:
            self.cannon_balls.empty()
            self._create_fleet()
            
    def ship_fx(self, direction):
        mySFX = pygame.mixer.Sound('pirate_fleet/media/splash.wav')
        match direction:
            case 'up':
                self.ship.moving_up = True
            case 'down':
                self.ship.moving_down = True
            case 'left':
                self.ship.moving_left = True
            case 'right':
                self.ship.moving_right = True
        pygame.mixer.Sound.play(mySFX)
        
    def _create_pirate(self, x_num, y_num):
        pirate = Pirate(self)
        pirate.rect.x = x_num
        pirate.rect.y = y_num
        self.pirates.add(pirate)
    
    def _create_fleet(self):
        num_pirates = self.settings.num_pirates
        for pirate in range(num_pirates):
            ran_x = random.randint(100,1500)
            ran_y = random.randint(50,850)
            self._create_pirate(ran_x, ran_y)
    
    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.pirates.empty()
            self.cannon_balls.empty()
            self._create_fleet()
            self.ship.center_ship()
        
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
        
    def _update_pirates(self):
        if pygame.sprite.spritecollideany(self.ship, self.pirates):
            self._ship_hit()
    
            
    """
    def _create_fleet(self):
        pirate = Pirate(self)
        pirate_width, pirate_height = pirate.rect.size
        available_space_x = self.settings.screen_width - (5 * pirate_width)
        number_pirate_x = available_space_x // (2 *pirate_width)
        
        
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (1 * pirate_height) - ship_height)
        number_rows = available_space_y // (2 *pirate_height)
        

        for row_number in range(number_rows):
            for pirate_number in range(number_pirate_x): 
                self._create_pirate(pirate_number, row_number)
                
    def _create_pirate(self, pirate_number, row_number):
        
        pirate = Pirate(self)
        pirate_width, pirate_height = pirate.rect.size
        pirate.x = pirate_width + 2 * pirate_width * pirate_number
        pirate.rect.x = pirate.x
        pirate.rect.y = pirate.rect.height + 2 * pirate.rect.height * row_number
        self.pirates.add(pirate)
            
    def _update_pirates(self):

        self._check_fleet_edges()
        self.pirates.update()

    
    def _check_fleet_edges(self):

        for pirate in self.pirates.sprites():
            if pirate.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        for pirate in self.pirates.sprites():
            pirate.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_drop_speed *= -1
        self.settings.fleet_direction *= -1 
    """
    
    
        
                      

if __name__=='__main__':
    
    ai = PirateFleet()
    ai.run_game()
    
    