from pygame import math as gmath
import random
import math

class Stars3D(object):

    def __init__(self, count, spread, speed):
        self.count = count
        self.spread = spread
        self.speed = speed

        self.fov = 140.0
        self.tanHalfFOV = float(math.tan(math.radians(self.fov / 2.0)))

        self.stars = []
        self.colors = []

    def getRandomStarPosition(self):
        rx = 2 * (random.uniform(0, 1) - 0.5) * self.spread
        ry = 2 * (random.uniform(0, 1) - 0.5) * self.spread
        rz = (random.uniform(0, 1) + 0.00001) * self.spread

        return gmath.Vector3(rx, ry, rz)

    def initStar(self, index):
        self.stars[index] = self.getRandomStarPosition()

    def initStars(self):
        self.stars = []

        for i in range(self.count):
            self.stars.append(self.getRandomStarPosition())
            self.colors.append((random.randrange(0,255),random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))

    def updateStars(self, renderWindow):
        for i in range(self.count):
            self.stars[i].z -= self.speed

            d = self.stars[i].z * self.tanHalfFOV

            x = int((self.stars[i].x / d) * 400 + 400)
            y = int((self.stars[i].y / d) * 300 + 300)

            if x < 0 or x >= 800 or y < 0 or y >= 600 or self.stars[i].z <= 0:
                self.initStar(i)
                continue

            renderWindow.set_at((x, y), self.colors[i])