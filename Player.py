import math
import pygame

class Player(object):

    def __init__(self, x, y, angle):
        self.posX = x
        self.posY = y

        self.dirAngle = angle
        self.dirX = 0
        self.dirY = 0
        self.fov = 60.0

        self.initPlayer()

    def initPlayer(self):
        self.setDirectionByAngle(self.dirAngle)

    def getAngleDirection(self):
        return self.dirAngle

    def setAngleDirection(self, angle):
        self.dirAngle = angle

    def setDirectionByAngle(self, angle):
        self.dirAngle = angle
        self.getDirection()

    def getDirection(self):
        self.dirX = math.cos(math.radians(self.dirAngle))
        self.dirY = math.sin(math.radians(self.dirAngle))

        return [self.dirX, self.dirY]

    def getPosition(self):
        return [self.posX, self.posY]

    def moveForward(self, multiplier):
        dir = self.getDirection()

        self.posX += dir[0] * multiplier
        self.posY += dir[1] * multiplier

    def drawPlayer(self, renderWindow):
        screenX = int((self.posX / 10) * 800)
        screenY = int((self.posY / 10) * 600)
        renderWindow.set_at((screenX, screenY), (255, 255, 255, 255))