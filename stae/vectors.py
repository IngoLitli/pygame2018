import math
class Vector2d():
    def __init__(self, startPoint, endPoint):
        self.start = {"x": startPoint[0], "y": startPoint[1]}
        self.end = {"x": endPoint[0], "y": endPoint[1]}
        self.v = [(self.end["x"]-self.start["x"]),(self.end["y"]-self.start["y"])]
        self.length = math.sqrt((math.pow(self.v[0],2))+(math.pow(self.v[1],2)))

    def unitVector(self):
        if self.start != self.end:
            return ((self.v[0] / self.length),(self.v[1] / self.length))
        else:
            return (0,0)

def addVector(vectorA, vectorB):
    return [(vectorA.v[0]+vectorB.v[0]),(vectorA.v[1]+vectorB.v[1])]

point1 = (0,0)
point2 = (1,0)
point3 = (-1,3)

vector1 = Vector2d(point1, point2)
vector2 = Vector2d(point1,point3)

print(vector1.v,vector2.v, addVector(vector1,vector2))