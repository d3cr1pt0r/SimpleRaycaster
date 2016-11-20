import math
width = 10
height = 10

map = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 2, 1,
    1, 0, 0, 0, 0, 0, 0, 2, 0, 1,
    1, 0, 0, 0, 0, 0, 2, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
]

color_map = {
    0: (0,0,0),
    1: (255, 255, 255),
    2: (255, 0, 0),
    3: (0, 255, 0),
    4: (0, 0, 255)
}

def getDistance(x1, y1, x2, y2):
    return math.hypot(x1-x2, y1-y2)

def getCellValue(posX, posY):
    return map[posX + posY * width]

def getCellPosition(posX, posY):
    return [int(posX), int(posY)]

def ray(posX, posY, dirX, dirY):
    hit = 0
    mapPos = getCellPosition(posX, posY)
    mapPosX = mapPos[0]
    mapPosY = mapPos[1]
    dirX2 = dirX * dirX
    dirY2 = dirY * dirY
    deltaDistX = math.sqrt(1 + dirY2 / dirX2)
    deltaDistY = math.sqrt(1 + dirX2 / dirY2)

    if dirX < 0:
        stepX = -1
        sideDistX = (posX - mapPosX) * deltaDistX
    else:
        stepX = 1
        sideDistX = (mapPosX + 1.0 - posX) * deltaDistX

    if dirY < 0:
        stepY = -1
        sideDistY = (posY - mapPosY) * deltaDistY
    else:
        stepY = 1
        sideDistY = (mapPosY + 1.0 - posY) * deltaDistY

    while hit == 0:
        if sideDistX < sideDistY:
            sideDistX += deltaDistX
            mapPosX += stepX
            side = 0
        else:
            sideDistY += deltaDistY
            mapPosY += stepY
            side = 1
        if map[mapPosX + mapPosY * width] > 0:
            hit = map[mapPosX + mapPosY * width]

    if side == 0:
        distance = (mapPosX - posX + (1 - stepX) / 2) / dirX
    else:
        distance = (mapPosY - posY + (1 - stepY) / 2) / dirY

    return [distance, color_map[hit]]