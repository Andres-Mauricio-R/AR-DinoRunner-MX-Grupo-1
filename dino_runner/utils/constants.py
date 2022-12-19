import pygame
import os

# Global Constants
pygame.mixer.init()
pygame.mixer.set_reserved(1)
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(ASSETS_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoRun2Hammer.png")),
]

JUMPING = pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoJump.png"))
DEATH = pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoDead.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Bird/Bird2.png")),
]

CLOUD = [
    pygame.image.load(os.path.join(ASSETS_DIR, 'Other/Cloud.png')),
    pygame.image.load(os.path.join(ASSETS_DIR, 'Other/Cloud1.png')),
    pygame.image.load(os.path.join(ASSETS_DIR, 'Other/Cloud2.png')),
]
SHIELD = pygame.image.load(os.path.join(ASSETS_DIR, 'Other/shield.png'))
FUNGU = pygame.image.load(os.path.join(ASSETS_DIR, 'Other/hongo.png'))
HAMMER = pygame.image.load(os.path.join(ASSETS_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(ASSETS_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(ASSETS_DIR, 'Other/SmallHeart.png'))

BACKGROUND_SOUND = pygame.mixer.Sound(os.path.join(ASSETS_DIR, 'sounds/background.ogg'))
BREAK_SOUND = pygame.mixer.Sound(os.path.join(ASSETS_DIR, 'sounds/break.ogg'))
HAMMER_SOUND = pygame.mixer.Sound(os.path.join(ASSETS_DIR, 'sounds/hammer.mp3'))
DAMAGE_SOUND = pygame.mixer.Sound(os.path.join(ASSETS_DIR, 'sounds/damage.ogg'))
JUMP_SOUND = pygame.mixer.Sound(os.path.join(ASSETS_DIR, 'sounds/jump.ogg'))
LIFE_SOUND = pygame.mixer.Sound(os.path.join(ASSETS_DIR, 'sounds/life.ogg'))
SHIELD_SOUND = pygame.mixer.Sound(os.path.join(ASSETS_DIR, 'sounds/shield.ogg'))
DAMAGE_SOUND = pygame.mixer.Sound(os.path.join(ASSETS_DIR, 'sounds/damage.ogg'))
DUCKING_SOUND = pygame.mixer.Sound(os.path.join(ASSETS_DIR, 'sounds/duck.mp3'))

DEFAULT_TYPE = "default"
HEART_COUNT = 5
SHIELD_TYPE = "shield"
FUNGU_TYPE = "fungu"
HAMMER_TYPE = "hammer"
