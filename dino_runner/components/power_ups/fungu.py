from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import FUNGU, DEFAULT_TYPE


class Fungu(PowerUp):
    def __init__(self):
        self.image = FUNGU
        self.type = DEFAULT_TYPE

        super().__init__(self.image, self.type)
