
class WumpsGame: #(Object):

    def __init__(self):
        self.playerList = []
        self.turnDict = {}
        self.roundrunning = False
        self.roundended = False
        self.whosFucked = ""
        self.pointer = 0
        self.roundcounter = 0

    def reset(self):
        self.playerList = []
        self.roundcounter = 0
        self.roundrunning = False
        self.roundended = False
        self.turnDict = {}

    def addName(self, name):
        self.playerList.append(name)

    def takeTurn(self, playerName, turn):
        if not self.roundrunning:
            # Start round:
            self.roundrunning = True
            self.roundended = False
            self.turnDict = {}
            for name in self.playerList:
                self.turnDict[name] = -1

        if self.turnDict[playerName] == -1:
            self.turnDict[playerName] = int(turn)

        allSet = True
        for name in self.turnDict:
            if self.turnDict[name] == -1:
                allSet = False
                break
        if allSet:
            self.endround()

    def endround(self):
        if self.roundrunning:
            self.roundcounter = self.roundcounter + 1
            self.roundrunning = False
            self.roundended = True
            for name in self.turnDict:
                if self.turnDict[name] == -1:
                    print("The Rount wasnt finished yet!")
                    return

                self.pointer = self.pointer + self.turnDict[name]
                self.turnDict[name] = -1
                if self.pointer >= len(self.playerList):
                    self.pointer = 0

            self.whosFucked = self.playerList[self.pointer]





