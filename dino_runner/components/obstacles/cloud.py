from dino_runner.components.obstacles.obstacle import Obstacle


import random

class Cloud(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = random.randint(25, 150)
        ##self.velocity = self.decide_velocity()
        self.velocity = random.randint(-20, 10)
    def decide_velocity(self):
      decide_velocit = random.randint(0,1)
      if decide_velocit == 0: # si es positvo
        return random.randint(-10,10)
      else:# si es negativo
        return random.randint(0,10) * -1;
        

