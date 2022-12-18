import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.cloud import Cloud
import pygame
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import BREAK_SOUND,DAMAGE_SOUND, CLOUD



class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.obstacles_cloud = []
        

    def update_cloud(self,game):
        if len(self.obstacles_cloud) == 0:
            object_type = random.randint(0,5)
            if  object_type == 0:
                self.obstacles_cloud.append(Cloud(CLOUD))
                # cambia el movimiento de los obstaculos de las nuevas
        for obstacle_cloud in self.obstacles_cloud:
            obstacle_cloud.update(game.game_speed + obstacle_cloud.velocity, self.obstacles_cloud)
    def update(self, game):
        if len(self.obstacles) == 0:
            object_type = random.randint(0,2)
            if object_type == 0:
                largeCactus = Cactus(LARGE_CACTUS)
                largeCactus.rect.y = 305 
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif object_type == 2:
                self.obstacles.append(Bird(BIRD))
            else:
                smallCactus = Cactus(SMALL_CACTUS)
                smallCactus.rect.y = 325
                self.obstacles.append(Cactus(SMALL_CACTUS))
                
        for obstacle in self.obstacles:
            # se colocan las velocidades a los obstaculo
            obstacle.update(game.game_speed, self.obstacles)
            ## cuando no tengo escudos
            if game.player.dino_rect.colliderect(obstacle.rect) and game.player.shield == False: #si te chocas con algo y no tenes activo el escudo
                BREAK_SOUND.stop()
                DAMAGE_SOUND.play()
                game.player_heart_manager.reduce_heart()

                if game.player_heart_manager.heart_count > 0:
                    print(f"VIDAS {game.player_heart_manager.heart_count}")
                    self.obstacles.pop()
                else:
                    game.player.death();
                    pygame.time.delay(500)
                    self.obstacles.remove(obstacle)
                    game.playing = False
                    game.death_count += 1
                    break
            if game.player.dino_rect.colliderect(obstacle.rect) and game.player.shield == True: #si  te chocas con algo y tenes activo el escudo
                if game.player_heart_manager.heart_count > 0:
                    BREAK_SOUND.play()
                    self.obstacles.pop()


    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    def draw_cloud(self, screen):
        for obstacle_cloud in self.obstacles_cloud:
            print(f"CLOUD {len(self.obstacles_cloud)}")
            obstacle_cloud.draw(screen)