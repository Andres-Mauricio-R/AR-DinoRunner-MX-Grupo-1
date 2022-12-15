import random
from dino_runner.components.obstacles.cactus import Cactus
import pygame
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    
    def update(self, game):
        if len(self.obstacles) == 0:
            cactus_size = random.randint(0,1)
            if cactus_size == 0:
                largeCactus = Cactus(LARGE_CACTUS)
                largeCactus.rect.y = 305 
                self.obstacles.append(Cactus(LARGE_CACTUS))
            else:
                smallCactus = Cactus(SMALL_CACTUS)
                smallCactus.rect.y = 325
                self.obstacles.append(Cactus(SMALL_CACTUS))


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect): #si hubo un choque retorna true
                pygame.time.delay(500)
                game.playing = False
                break


    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)