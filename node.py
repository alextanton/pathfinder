

class node():
    def __init__(self, rect, p1, p2, name, pointsTo):
        self.rect = rect
        self.p1 = p1
        self.p2 = p2
        self.name = name
        self.pointsTo = pointsTo

    def setPoints(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def addLines(self, lines):
        i=0
        newpt = []
        for p in self.pointsTo:
            y = (p, lines[i])
            newpt.append(y)
            i += 1
        self.pointsTo = newpt
