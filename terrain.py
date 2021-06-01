import pygame, random, numpy as np
pygame.init()

WORLD_LENGTH = 24
WORLD_HEIGHT = 16
SEA_LEVEL = 25
MEAN_HEIGHT = 7

PLAINS = random.randint(-1,1)

game = pygame.display.set_mode((WORLD_LENGTH*48,WORLD_HEIGHT*48))
pygame.display.set_caption("Discount Minecraft")
clock = pygame.time.Clock()

# 0 = air, 1 = dirt, 2 = grass, 3 = stone
dirt = pygame.image.load('assets/dirt.png')
dirt_grass = pygame.image.load('assets/dirt_grass.png')
stone = pygame.image.load('assets/stone.png')

world = np.zeros((WORLD_LENGTH,WORLD_HEIGHT))
#world = [[0]*WORLD_HEIGHT]*WORLD_LENGTH

class worldGenerator():
    def __init__(self):
        pass
# 0 = air, 1 = dirt, 2 = grass, 3 = stone
    def generate():
        RandomHeight = MEAN_HEIGHT
        for x in range(WORLD_LENGTH):
            RandomHeight += random.randint(-1,1)
            DirtHeight = random.randint(3,4)
            for y in range(RandomHeight, WORLD_HEIGHT):
                if y == RandomHeight:
                    world[x][y] = 2
                elif y - DirtHeight < RandomHeight:
                    world[x][y] = 1
                else:
                    world[x][y] = 3

    def generateOre():
        pass

    def draw():
        for x in range(WORLD_LENGTH):
            for y in range(WORLD_HEIGHT):
                if world[x][y] == 1:
                    game.blit(dirt,(x*48,y*48))
                elif world[x][y] == 2:
                    game.blit(dirt_grass,(x*48,y*48))
                elif world[x][y] == 3:
                    game.blit(stone,(x*48,y*48))

game.fill((102,255,255))
worldGenerator.generate()
worldGenerator.draw()

run = True
while run:
    clock.tick(24)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False