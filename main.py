import numpy.random
import pygame, sys
import numpy as np
from ZOA import *
from pygame.examples import scroll

INCREMENT_UNIT = 8
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
DARKBLUEBACK = (13, 13, 27)
LAVENDERBORDER = (17, 17, 31)
ELEMENT_COLOR_MAP = {"X": DARKBLUEBACK, "BA": (148, 201, 167)}
WIDTH = 1520
HEIGHT = 1008
xBoxes = 189
yBoxes = 125
CENTRAL_COSM_DATA = np.zeros([xBoxes, yBoxes])

class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, ID):
        super().__init__()
        self.ID = ID
        self.ENERGYLEVEL = 1
        self.x = x
        self.y = y
        self.color = ELEMENT_COLOR_MAP[ID]
        self.rect = pygame.Rect(1+8*(self.x) , 1+8*(self.y), INCREMENT_UNIT - 2, INCREMENT_UNIT - 2)
        pygame.draw.rect(SCREEN, self.color, self.rect)
    def getID(self):
        return self.i
    def update(self):
        self.rect = self.rect.move(2*INCREMENT_UNIT, 2*INCREMENT_UNIT)
        pygame.draw.rect(SCREEN, self.color, self.rect)
    def delete(self):
        pygame.draw.rect(SCREEN, DARKBLUEBACK, self.rect)
    def move(self, direction):
        if direction == "LEFT":
            pygame.draw.rect(SCREEN, DARKBLUEBACK, pygame.Rect(1 + 8 * (self.x), 1 + 8 * (self.y), INCREMENT_UNIT - 2, INCREMENT_UNIT - 2))
            self.x -= 1
            pygame.draw.rect(SCREEN, self.color, (1 + 8 * (self.x), 1 + 8 * (self.y), INCREMENT_UNIT - 2, INCREMENT_UNIT - 2))
        if direction == "RIGHT":
            pygame.draw.rect(SCREEN, DARKBLUEBACK, pygame.Rect(1 + 8 * (self.x), 1 + 8 * (self.y), INCREMENT_UNIT - 2, INCREMENT_UNIT - 2))
            self.x += 1
            pygame.draw.rect(SCREEN, self.color, (1 + 8 * (self.x), 1 + 8 * (self.y), INCREMENT_UNIT - 2, INCREMENT_UNIT - 2))
        if direction == "DOWN":
            pygame.draw.rect(SCREEN, DARKBLUEBACK, pygame.Rect(1+8*(self.x) , 1+8*(self.y), INCREMENT_UNIT - 2, INCREMENT_UNIT - 2))
            self.y += 1
            pygame.draw.rect(SCREEN, self.color, (1+8*(self.x) , 1 + 8*(self.y), INCREMENT_UNIT - 2, INCREMENT_UNIT - 2))
        if direction == "UP":
            pygame.draw.rect(SCREEN, DARKBLUEBACK, pygame.Rect(1 + 8 * (self.x), 1 + 8 * (self.y), INCREMENT_UNIT - 2, INCREMENT_UNIT - 2))
            self.y -= 1
            pygame.draw.rect(SCREEN, self.color, (1 + 8 * (self.x), 1 + 8 * (self.y), INCREMENT_UNIT - 2, INCREMENT_UNIT - 2))
    def moveRandom(self):
        Dict = {0: "DOWN", 1: "UP", 2: "LEFT", 3: "RIGHT"}
        randomNum = np.random.randint(0, 4)
        self.move(Dict[randomNum])
def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("LifeEngine ||| VERSION 0.0.1 ||| Cosm 1 ")
    CLOCK = pygame.time.Clock()
    SCREEN.fill(DARKBLUEBACK)
    drawGrid(WIDTH, HEIGHT)
    container = pygame.sprite.Group()
    for i in range(50):
        x = np.random.randint(0, xBoxes)
        y = np.random.randint(0, yBoxes)
        newGuy = Particle(x, y, "BA")
        container.add(newGuy)
    agent_container = pygame.sprite.Group()
    for i in range(10):
        x = np.random.randint(0, xBoxes)
        y = np.random.randint(0, yBoxes)
        newGuy = Particle(x, y, "AA")
        agent_container.add(newGuy)
    #guy = Particle(60, 60, "AA")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for pygame.sprite in agent_container.sprites():
            pygame.sprite.moveRandom()
        pygame.display.flip()
        CLOCK.tick(1)
def drawGrid(W, H):
    blockSize = 16 #Set the size of the grid block
    for x in range(0, W, INCREMENT_UNIT):
        for y in range(0, H, INCREMENT_UNIT):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, LAVENDERBORDER, rect, 1)


def ZOA_TEST_1():
    COSM_UNIT = 8
    COSM_WIDTH = 500
    COSM_HEIGHT = 500
    print("running ZOA Test 1")
    world1 = Cosm("COSM1TEST1", COSM_HEIGHT, COSM_WIDTH, COSM_UNIT)
    session1 = Session(world1, 1)
    session1.runSession()


ZOA_TEST_1()




# THE PLAN
# COSMS are windows of simulation. All biological processes take place within a COSM
# ARM - Artificial Replication Metadata - Digital DNA
#
#data is stored in central cosm data array and displayed on pygame cosm window
#each tick, wait for all data to compute before updating graphics
#
# elements are coded [LETTER, LETTER, NUMBER] (i.e. AA4) the first two letters are element symbol, and the second is concurrent energy level
#
# DO NOT TREAT CELLS AS HOLLOW BODIES TREAT THEM AS BLOBS THAT GET STUFF PROGRESSIVELY STUCK ON THEM AS THEY GROW> THIS WAY MOVEMENT IS SIMPLER ETC.