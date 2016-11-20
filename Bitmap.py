class Bitmap(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.clear()

    def clear(self):
        self.components = bytearray(self.width * self.height * 4)

    def setPixel(self, x, y, r, g, b, a):
        index = (x + y * self.width) * 4

        self.components[index] = r
        self.components[index + 1] = g
        self.components[index + 2] = b
        self.components[index + 3] = a

    def getPixel(self, x, y):
        return [
            self.components[x + y * self.width],
            self.components[x + y * self.width + 1],
            self.components[x + y * self.width + 2],
            self.components[x + y * self.width + 3]
        ]