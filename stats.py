class stats0:  
    def __init__(self, _health, _luck, _reputation):
        self._health = _health
        self._luck = _luck
        self._reputation = _reputation

    def getluck(self):
        return self._luck
    def setluck(self, newluck):
        self.luck = newluck
    def gethealth(self):
        return self._health
    def sethealth(self, newhealth):
        self._health = newhealth
    def getreputation(self):
        return self._reputation
    def setreputation(self, newreputation):
        self._reputation = newreputation