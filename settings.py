# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1024  # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "ExtraTerrestial Platformer"
BGCOLOR = DARKGREY
CAMERA_SMOOTHNESS_FACTOR = 0.06

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
# Player settings

PLAYER_GRAVITY = 0.5
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_JUMP = -15
PLAYER_SPRITESHEET = "spritetest1.png"
PLAYER_STANDING = (48, 0, 48, 56)
