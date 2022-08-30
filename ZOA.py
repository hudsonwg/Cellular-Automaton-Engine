#EMPTY SQUARES DENOTED BY "X"
#SWEEPERS ARE OBJECTS THAT ARE AT RISK OF TURNING TO X UNLESS ANOTHER OBJECT FILLS THEIR PLACE. ONCE ALL OBJECTS ARE MOVED ANY OUTSTANDING SWEEPERS ARE CONVERTED TO "X"
#CLASS OBJECTS FOR ZOA PYTHON LIBRARY
#SEED IS LOCATION OF ARM BUNDLE AND CORTICAL PROTEIN RESPECTIVELY  EXAMPLE: {[0, 1], [0, 2]}


#TYPES OF ACTION - - - - - MOVEMENT, EAT, ATTACK, REPOSITION, STORE/COLLECT,
class Cosm:
    def __init__(self, centralData, elements, ID, height, width):
        self.COSM_CENTRAL_DATA = centralData
        self.COSM_ELEMENT_TABLE = elements
        self.COSM_ID = ID
        self.COSM_HEIGHT = height
        self.COSM_WIDTH = width
        self.SWEEP_INDEXES = []
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
    def moveOrganism(organismArray, Direction):
        print("under construction")
    def updateSweepers(self):
        for index in self.SWEEP_INDEXES:
            if(self.COSM_CENTRAL_DATA[index][-1] == "X" and len(self.COSM_CENTRAL_DATA[index]) != 1):
                self.COSM_CENTRAL_DATA[index] = "X"
        self.SWEEP_INDEXES = []
    def updateCosm(self):
        print("under construction")
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