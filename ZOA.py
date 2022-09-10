import numpy
import pygame
import sys


##CONSTANTS##
COLORKEY = {"BLACK": (0, 0, 0), "WHITE": (255, 255, 255), "BLUE": (0, 100, 255), "DARKBLUE": (13, 13, 27)}
CODEKEY = {"AAA": (13, 13, 27),"BAA": (0, 100, 255), "CAA": (255, 255, 255), "DAA": (96, 235, 152), "EAA": (245, 51, 196)}
GENERATEKEY = ["BAA", "CAA", "DAA", "EAA"]

##CLASSES##
class Session:
    def __init__(self, cosm, tick, borders, randomOrganisms):
        self.randomOrganisms = randomOrganisms
        self.borders = borders
        self.borderVal = 0
        self.tickSpeed = tick
        global SCREEN, CLOCK
        self.cosm = cosm
        pygame.init()
        SCREEN = pygame.display.set_mode((cosm.COSM_HEIGHT*cosm.increment, cosm.COSM_WIDTH*cosm.increment))
        pygame.display.set_caption("LifeEngine ||| VERSION 0.0.1 ||| Cosm 1 ")
        CLOCK = pygame.time.Clock()
    def runSession(self):
        if(self.borders == True):
            borderVal = 0.1
        else:
            borderVal = 0
        ##DECLARE RANDOM ORGS
        if(self.randomOrganisms == True):
            organismArray = []
            organismArray.append(randomOrganism("001", self.cosm, 10))
            organismArray.append(randomOrganism("002", self.cosm, 10))
            organismArray.append(randomOrganism("003", self.cosm, 10))
            organismArray.append(randomOrganism("004", self.cosm, 10))
            organismArray.append(randomOrganism("005", self.cosm, 10))
            organismArray.append(randomOrganism("006", self.cosm, 10))
            organismArray.append(randomOrganism("007", self.cosm, 10))
            organismArray.append(randomOrganism("008", self.cosm, 10))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.cosm.updateCosm()
            #DISPLAY ORGANISMS
            if(self.randomOrganisms == True):
                for org in organismArray:
                    org.move()
            ##DRAWS ARRAY ON UPDATE
            for i in range(self.cosm.COSM_HEIGHT):
                for j in range(self.cosm.COSM_WIDTH):
                    ##THE -2 clauses in the line below represent the width of the grids
                    rect = pygame.Rect(1 + self.cosm.increment * (j), 1 + self.cosm.increment * (i), self.cosm.increment - borderVal, self.cosm.increment - borderVal)
                    pygame.draw.rect(SCREEN, CODEKEY[self.cosm.COSM_CENTRAL_DATA[i][j][3:6]], rect)

            pygame.display.flip()
            CLOCK.tick(self.tickSpeed)
class Cosm:
    def __init__(self, ID, width, height, increment):
        self.increment = increment
        #self.COSM_CENTRAL_DATA = [["X"] * width] * height
        self.COSM_CENTRAL_DATA = numpy.full([width, height], "000AAA")
        self.COSM_ELEMENT_TABLE = 0
        self.COSM_ID = ID
        self.COSM_HEIGHT = height
        self.COSM_WIDTH = width
        self.SWEEP_INDEXES = []
    def changeIndex(self, x, y, change):
        self.COSM_CENTRAL_DATA[y][x] = change
    def data(self):
        print(self.COSM_CENTRAL_DATA)
        print(self.COSM_ELEMENT_TABLE)
        print(self.COSM_ID)
        print(self.COSM_HEIGHT)
        print(self.COSM_WIDTH)
    def moveElement(self, inputIndex, Direction):
        current = self.COSM_CENTRAL_DATA[inputIndex[0], inputIndex[1]]
        # check if queried space is empty
        if Direction == "LEFT":
            if(inputIndex[1] > 0 and (self.COSM_CENTRAL_DATA[inputIndex[1]-1])[-1] == "X"):
                self.COSM_CENTRAL_DATA[inputIndex[0], (inputIndex[1]-1)]
                self.COSM_CENTRAL_DATA[inputIndex[0], (inputIndex[1])] += "X"
                self.SWEEP_INDEXES.append([(inputIndex[0], (inputIndex[1]))])
        if Direction == "RIGHT":
            if (inputIndex[1] < self.COSM_WIDTH - 1 and (self.COSM_CENTRAL_DATA[inputIndex[1] + 1])[-1] == "X"):
                self.COSM_CENTRAL_DATA[inputIndex[0], (inputIndex[1] + 1)]
                self.COSM_CENTRAL_DATA[inputIndex[0], (inputIndex[1])] += "X"
                self.SWEEP_INDEXES.append([inputIndex[0], (inputIndex[1])])
        if Direction == "DOWN":
            if (inputIndex[0] > 0 and (self.COSM_CENTRAL_DATA[inputIndex[0] + 1])[-1] == "X"):
                self.COSM_CENTRAL_DATA[inputIndex[0] + 1, (inputIndex[1])]
                self.COSM_CENTRAL_DATA[inputIndex[0], (inputIndex[1])] += "X"
                self.SWEEP_INDEXES.append([inputIndex[0], (inputIndex[1])])
        if Direction == "UP":
            if (inputIndex[0] < self.COSM_HEIGHT-1 and (self.COSM_CENTRAL_DATA[inputIndex[0] - 1])[-1] == "X"):
                self.COSM_CENTRAL_DATA[inputIndex[0] - 1, (inputIndex[1])]
                self.COSM_CENTRAL_DATA[inputIndex[0], (inputIndex[1])] += "X"
                self.SWEEP_INDEXES.append([inputIndex[0], (inputIndex[1])])
    def moveOrganism(organismArray, Direction, Velocity):
        #velocity is determined by total negative mass of organism (-m) + its locomotive coefficient (LOCOCO)
        #It's a large spatula, and we all live on it, but when you climb through the divots to the other side and the spatula does not flip, you live backwards


        print("under construction")
    def updateSweepers(self):
        for index in self.SWEEP_INDEXES:
            if(self.COSM_CENTRAL_DATA[index][-1] == "X" and len(self.COSM_CENTRAL_DATA[index]) != 1):
                self.COSM_CENTRAL_DATA[index] = "X"
        self.SWEEP_INDEXES = []
    def updateCosm(self):
        print("updating cosm")
class Organism:
    def __init__(self, ARM, Seed):
        self.ARM = ARM
        self.Seed = Seed
        self.ElementArray = []
        #make sure to initialize element array with seed
    def addElement(self, Element, Location):
        if(Element.getConnection() == False):
            Element.toggleConnection()
    def completeAction(self):
        print("under construction")
class randomOrganism:
    def __init__(self, ID, cosm, size):
        self.elArray = []
        self.ID = ID
        self.size = size
        self.cosm = cosm

        rootFound = False
        while(rootFound == False):
            randRoot1 = numpy.random.randint(0, cosm.COSM_HEIGHT - 1)
            randRoot2 = numpy.random.randint(0, cosm.COSM_WIDTH - 1)
            if(cosm.COSM_CENTRAL_DATA[randRoot1][randRoot2] == "000AAA"):
                randKey = numpy.random.randint(0, 3)
                cosm.COSM_CENTRAL_DATA[randRoot1][randRoot2] = (ID + GENERATEKEY[randKey])
                self.elArray.append([randRoot1, randRoot2])
                rootFound = True
        try:
            if (cosm.COSM_CENTRAL_DATA[self.elArray[0][0]][self.elArray[0][1] + 1] == "000AAA"):
                favor = numpy.random.randint(0, 10)
                if(favor < 8):
                    cosm.COSM_CENTRAL_DATA[self.elArray[0][0]][self.elArray[0][1] + 1] = "000CAA"
                    self.elArray.append([self.elArray[0][0], self.elArray[0][1] + 1])
        except:
            print("something shorted")
        try:
            if (cosm.COSM_CENTRAL_DATA[self.elArray[0][0]][self.elArray[0][1] - 1] == "000AAA"):
                favor = numpy.random.randint(0, 10)
                if(favor < 8):
                    cosm.COSM_CENTRAL_DATA[self.elArray[0][0]][self.elArray[0][1] - 1] = "000CAA"
                    self.elArray.append([self.elArray[0][0], self.elArray[0][1] - 1])
        except:
            print("something shorted")
        try:
            if (cosm.COSM_CENTRAL_DATA[self.elArray[0][0] + 1][self.elArray[0][1] + 1] == "000AAA"):
                favor = numpy.random.randint(0, 10)
                if(favor < 8):
                    cosm.COSM_CENTRAL_DATA[self.elArray[0][0] + 1][self.elArray[0][1] + 1] = "000CAA"
                    self.elArray.append([self.elArray[0][0] + 1, self.elArray[0][1] + 1])
        except:
            print("something shorted")
        try:
            if (cosm.COSM_CENTRAL_DATA[self.elArray[0][0] - 1][self.elArray[0][1] + 1] == "000AAA"):
                favor = numpy.random.randint(0, 10)
                if(favor < 8):
                    cosm.COSM_CENTRAL_DATA[self.elArray[0][0] - 1][self.elArray[0][1] + 1] = "000CAA"
                    self.elArray.append([self.elArray[0][0] - 1, self.elArray[0][1] + 1])
        except:
            print("something shorted")
        try:
            if (cosm.COSM_CENTRAL_DATA[self.elArray[0][0] - 1][self.elArray[0][1] - 1] == "000AAA"):
                favor = numpy.random.randint(0, 10)
                if(favor < 8):
                    cosm.COSM_CENTRAL_DATA[self.elArray[0][0] - 1][self.elArray[0][1] - 1] = "000CAA"
                    self.elArray.append([self.elArray[0][0] - 1, self.elArray[0][1] - 1])
        except:
            print("something shorted")
        try:
            if (cosm.COSM_CENTRAL_DATA[self.elArray[0][0] - 1][self.elArray[0][1]] == "000AAA"):
                favor = numpy.random.randint(0, 10)
                if(favor < 8):
                    cosm.COSM_CENTRAL_DATA[self.elArray[0][0] - 1][self.elArray[0][1]] = "000CAA"
                    self.elArray.append([self.elArray[0][0] - 1, self.elArray[0][1]])
        except:
            print("something shorted")
        try:
            if (cosm.COSM_CENTRAL_DATA[self.elArray[0][0] + 1][self.elArray[0][1] - 1] == "000AAA"):
                favor = numpy.random.randint(0, 10)
                if(favor < 8):
                    cosm.COSM_CENTRAL_DATA[self.elArray[0][0] + 1][self.elArray[0][1] - 1] = "000CAA"
                    self.elArray.append([self.elArray[0][0] + 1, self.elArray[0][1] - 1])
        except:
            print("something shorted")
        try:
            if (cosm.COSM_CENTRAL_DATA[self.elArray[0][0] + 1][self.elArray[0][1]] == "000AAA"):
                favor = numpy.random.randint(0, 10)
                if(favor < 8):
                    cosm.COSM_CENTRAL_DATA[self.elArray[0][0] + 1][self.elArray[0][1]] = "000CAA"
                    self.elArray.append([self.elArray[0][0] + 1, self.elArray[0][1]])
        except:
            print("something shorted")

        #ADD RECURSIVE BUILD FUNCTION
        #make sure to initialize element array with seed
    def move(self):
        # 0 = left, 1 = right, 2 = down, 3 = up
        direction = 1
        canMove = True
        if(direction == 1):
            for coord in self.elArray:
                if(self.cosm.COSM_CENTRAL_DATA[coord[0]][coord[1] + 1] == "000AAA" and self.cosm.COSM_CENTRAL_DATA[coord[0]][coord[1] + 1][0:3] == self.ID):
                    #print(self.cosm.COSM_CENTRAL_DATA[coord[0]][coord[1] + 1][0:3])
                    #print("id = " + self.ID)
                    print(self.cosm.COSM_CENTRAL_DATA[coord[0]][coord[1] + 1] != "000AAA")
                    print(self.cosm.COSM_CENTRAL_DATA[coord[0]][coord[1] + 1][0:3] != self.ID)
                    canMove = False
            #MAKE NEW ARRAY
            #DELETE OLD ARRAY FROM COSM
            #ADD NEW ARRAY TO COSM AND MAKE IT THE OLD ARRAY IN CLASS
            if (canMove == True):
                print("hello")
                newArr = self.elArray
                for coord in newArr:
                    coord[1] += 1
                for coord in self.elArray:
                    self.cosm.COSM_CENTRAL_DATA[coord[0]][coord[1]] = "000AAA"
                self.elArray = newArr
                for coord in self.elArray:
                    self.cosm.COSM_CENTRAL_DATA[coord[0]][coord[1]] = "000CAA"
        print("moving")

class Ecosystem:
    def __init__(self, Organisms):
        self.organisms = Organisms
    def addOrganism(self, Organism):
        self.organisms.update(Organism)
class Element:
    def __init__(self, ID, Connected, INDEX):
        self.ID = ID
        self.connected = False
        self.elementIndex = INDEX
    def toggleConnection(self):
        if(self.connected == True):
            self.connected = False
        if(self.connected == False):
            self.connected = True
    def getConnection(self):
        return self.connected
    def getID(self):
        return self.ID
class Element_Table:
    def __init__(self, currentElements):
        #Pass in dictionary
        self.elementTable = currentElements
    def addElement(self, Element):
        #add to dictionary of elements
        self.elementTable.update(Element)


##ELEMENT FUNCTIONS##
def generateRandomFood(amount, cosm):
    count = 0
    while(count<amount):
        randx = numpy.random.randint(0, cosm.COSM_WIDTH)
        randy = numpy.random.randint(0, cosm.COSM_HEIGHT)
        if(cosm.COSM_CENTRAL_DATA[randx][randy] == "000AAA"):
            cosm.COSM_CENTRAL_DATA[randx][randy] = "000BAA"
            count += 1
def generateRandomElement(element, amount, cosm):
    count = 0
    while(count<amount):
        randx = numpy.random.randint(0, cosm.COSM_WIDTH)
        randy = numpy.random.randint(0, cosm.COSM_HEIGHT)
        if(cosm.COSM_CENTRAL_DATA[randx][randy] == "000AAA"):
            cosm.COSM_CENTRAL_DATA[randx][randy] = element
            count += 1
        #ADD RECURSIVE GROWTH
def drawParticle(xCoord, yCoord):
    ##will handle drawing single particle at single index
    print("FUNCTION - drawParticle() is currently under construction")
def deleteParticle(xCoord, yCoord):
    ##MAKES PARTICLE EMPTY SPACE AT SPECIFIC LOCATION
    print("FUNCTION - deleteParticle() is currently under construction")
def checkMoveQuery(currentX, currentY, queriedX, queriedY):
    ##check if proposed move is possible, or if there is collision, returns false if collisions detected
    moveApproved = False
    print("FUNCTION - checkMoveQuery() is currently under construction")





#GENERAL COSM STRUCTURE
#
#Cosm contains array of elements,
#once a part of an organism, elements are no longer controleld by the cosm but rather the organism
#organism calls action each tick to choose action. if organism moves, it passes a movement direction plus the array of its member elements to the cosm for the movement function to occur there.
#
#EMPTY SQUARES DENOTED BY "X"
#SWEEPERS ARE OBJECTS THAT ARE AT RISK OF TURNING TO X UNLESS ANOTHER OBJECT FILLS THEIR PLACE. ONCE ALL OBJECTS ARE MOVED ANY OUTSTANDING SWEEPERS ARE CONVERTED TO "X"
#CLASS OBJECTS FOR ZOA PYTHON LIBRARY
#SEED IS LOCATION OF ARM BUNDLE AND CORTICAL PROTEIN RESPECTIVELY  EXAMPLE: {[0, 1], [0, 2]}
#TYPES OF ACTION - - - - - MOVEMENT, EAT, ATTACK, REPOSITION, STORE/COLLECT,