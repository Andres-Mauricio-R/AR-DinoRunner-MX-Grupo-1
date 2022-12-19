import pygame
from asyncio import shield
import random

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.fungu import Fungu
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.utils.constants import LIFE_SOUND,SHIELD_SOUND, HAMMER_SOUND
class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appers = 0
        self.when_points = 0 


    def update(self, points, game_speed, player, player_heart_manager):

        # self.generate_power_ups(points)
        probalityGetPower = random.randint(0, 100) # Probabilidad que aparesca un escudo

        if probalityGetPower == 1: # Cuando el Numero rando sea igual a 1
            self.generate_power_ups(points)


        for powerup in self.power_ups:
            # verificar si el powerup es de tipo shield o de tipo Fungu
            powerup.update(game_speed, self.power_ups)
            if (player.dino_rect.colliderect(powerup.rect)):
                if isinstance(powerup, Hammer): # si es de tipo Martillo
                    HAMMER_SOUND.set_volume(0.2)
                    SHIELD_SOUND.stop()
                    HAMMER_SOUND.stop()
                    LIFE_SOUND.stop()
                    HAMMER_SOUND.play()
                    player.shield = True # Agarre el escudo
                    powerup.start_time = pygame.time.get_ticks() #temporizador
                    powerup.start_time = pygame.time.get_ticks()
                    player.shield_time_up = powerup.start_time + ((random.randint(5,8) * 1000)) #
                if  isinstance(powerup, Fungu): # si es de tipo Hongo
                    LIFE_SOUND.set_volume(0.2)
                    SHIELD_SOUND.stop()
                    HAMMER_SOUND.stop()
                    LIFE_SOUND.stop()
                    LIFE_SOUND.play()
                    player.shield = False # Agarre el escudo
                    player_heart_manager.add_heart() # Aumenta vida
                if isinstance(powerup, Shield): # Si es de Tipo Shield
                    SHIELD_SOUND.stop()
                    HAMMER_SOUND.stop()
                    LIFE_SOUND.stop()
                    SHIELD_SOUND.play()
                    player.shield = True
                    powerup.start_time = pygame.time.get_ticks() #temporizador
                    powerup.start_time = pygame.time.get_ticks()
                    player.shield_time_up = powerup.start_time + ((random.randint(5,8) * 1000)) #tiempo aleatorio en milisegundos
                player.type = powerup.type
                self.power_ups.remove(powerup)




    def draw(self, screen):
        for powerup in self.power_ups:
            powerup.draw(screen)


    def generate_power_ups(self, points):
        self.points = points
        if len(self.power_ups) == 0:
            # if self.when_appers == self.points:
                # self.when_appers == random.randint(self.when_appers + 150 , 500 +self.when_appers)
                random_power_ups_generate = random.randint(0, 2)
                if (random_power_ups_generate == 0 ):
                    self.power_ups.append(Shield())
                if (random_power_ups_generate == 1):
                    self.power_ups.append(Fungu())
                if (random_power_ups_generate == 2):
                    self.power_ups.append(Hammer())

