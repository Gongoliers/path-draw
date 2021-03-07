class SimplePath():

    def __init__(self):
        self.path = []

    def addRotation(self, degrees):
        self.path.append((degrees, True))

    def addStraightAway(self, distance):
        self.path.append((distance, False))
