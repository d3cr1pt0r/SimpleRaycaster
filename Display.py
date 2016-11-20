import pygame, random
from Bitmap import Bitmap

class Display(object):

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

        self.renderWindow = None
        self.frameBuffer = Bitmap(self.width, self.height)
        self.clearColor = (0,0,0)

        self.create()

    def create(self):
        pygame.init()
        pygame.display.set_caption(self.title)
        self.renderWindow = pygame.display.set_mode((self.width, self.height))

    def close(self):
        pygame.quit()
        quit()