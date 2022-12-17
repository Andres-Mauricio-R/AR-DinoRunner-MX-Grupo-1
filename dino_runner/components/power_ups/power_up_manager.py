from asyncio import shield
import random

from dino_runner.components.power_ups.shield import shield

class PowerUpManajer:
    def __init__(self):
        self.power_ups = []
        self.when_appers = 0 #me dice cuando quiero que aparescan


    def update(self, points, game_speed):
        self.generate_power_ups(points)
        for powerup in self.power_ups:
            powerup.update(game_speed,self.power_ups)



    def draw(self, screen):
        for powerup in self.power_ups:
            powerup.draw(screen)


    def generate_power_ups(self, points):
        self.points = points
        if len(self.power_ups) == 0:
            if self.when_appers == self.points:
                self.when_appers == random.randint(self.when_appers + 150 , 500 +self.when_appers)
                self.power_ups.append(shield())
            
