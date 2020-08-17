
class WumpsGame:

    def __init__(self):
        self.playerList = []
        self.turnDict = {}
        # Möglich: Pregame, In_Round, Round_End
        self.phase = "Pregame"
        self.whosFucked = ""
        self.pointer = 0
        self.roundcounter = 0

    def reset(self):
        self.playerList = []
        self.roundcounter = 0
        self.phase = "Pregame"
        self.turnDict = {}

    def addName(self, name):
        self.turnDict[name] = {'turn' : -1, 'fucked' : 0}
        self.playerList.append(name)
        self.phase = "Pregame"

    def takeTurn(self, playerName, turn):
        if not self.phase == "In_Round":
            # Start round:
            self.phase = "In_Round"
            for name in self.playerList:
                if name not in self.turnDict:
                    self.turnDict[name] = {'turn' : -1, 'fucked' : 0}
        print(self.turnDict)
        if self.turnDict[playerName]['turn'] == -1:
            self.turnDict[playerName]['turn'] = int(turn)

        allSet = True
        for name in self.turnDict:
            if self.turnDict[name]['turn'] == -1:
                allSet = False
                break
        if allSet:
            self.endround()

    def endround(self):
        if self.phase == "In_Round":
            self.roundcounter = self.roundcounter + 1
            self.phase = "Round_End"
            for name in self.turnDict:
                if self.turnDict[name]['turn'] == -1:
                    print("The Rount wasnt finished yet!")
                    return

                self.pointer = self.pointer + self.turnDict[name]['turn']
                self.turnDict[name]['turn'] = -1
                if self.pointer >= len(self.playerList):
                    self.pointer = 0

            self.whosFucked = self.playerList[self.pointer]
            self.turnDict[self.whosFucked]['fucked'] += 1





