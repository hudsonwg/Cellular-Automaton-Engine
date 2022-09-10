import numpy.random
import pygame, sys
import numpy as np
from ZOA import *
from pygame.examples import scroll

def ZOA_TEST_1():
    COSM_UNIT = 4
    COSM_WIDTH = 200
    COSM_HEIGHT = 200
    print("running ZOA Test 1")
    world1 = Cosm("COSM1TEST1", COSM_HEIGHT, COSM_WIDTH, COSM_UNIT)
    generateRandomFood(50, world1)
    generateRandomElement("000DAA", 20, world1)
    generateRandomElement("000EAA", 20, world1)
    world1.COSM_CENTRAL_DATA[50][50] = "000CAA"
    world1.COSM_CENTRAL_DATA[51][50] = "000CAA"
    world1.COSM_CENTRAL_DATA[51][51] = "000CAA"
    world1.COSM_CENTRAL_DATA[52][51] = "000CAA"
    session1 = Session(world1, 1, True)
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