import pygame
from Stars3D import Stars3D
from Player import Player
from Display import Display
import Map as map
import math

class MainGame(object):

    def __init__(self, width=800, height=600, title='Main Game'):
        self.display = Display(width, height, title)
        self.isGameRunning = False

        #self.stars = Stars3D(1000, 1, 0.001)
        #self.stars.initStars()

        self.player = Player(5, 5, 45)
        self.min_dist = 999999999

        self.start_time = 0
        self.end_time = 0
        self.delta_time = 0
        self.frames = 0
        self.fps = 0

    def start(self):
        if not self.isGameRunning:
            self.isGameRunning = True
            self.run()

    def run(self):
        while self.isGameRunning:
            self.poolEvents()
            self.render()

        self.display.close()

    def poolEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isGameRunning = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_dir = self.player.getDirection()
                    print map.ray(self.player.posX, self.player.posY, player_dir[0], player_dir[1])

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.setAngleDirection(self.player.getAngleDirection() - 100 * self.delta_time)
        if keys[pygame.K_RIGHT]:
            self.player.setAngleDirection(self.player.getAngleDirection() + 100 * self.delta_time)
        if keys[pygame.K_UP]:
            if self.min_dist > 0.5:
                self.player.moveForward(5 * self.delta_time)
        if keys[pygame.K_DOWN]:
            self.player.moveForward(-5 * self.delta_time)

    def render(self):
        self.start_time = pygame.time.get_ticks()

        self.display.renderWindow.fill(0)
        self.renderPerspectiveMap()
        pygame.display.update()

        self.delta_time = (self.start_time - self.end_time) / 1000.0
        self.end_time = self.start_time
        self.frames += 1
        self.fps = 1.0 / self.delta_time

    def renderPerspectiveMap(self):
        player_angle = self.player.getAngleDirection()
        start_angle = player_angle - self.player.fov / 2.0
        angle_step = self.player.fov / self.display.width
        target_angle = start_angle + self.player.fov
        screenX = 0
        wall_height = 300
        self.min_dist = 999999999

        while start_angle < target_angle:
            start_angle += angle_step
            dx = math.cos(math.radians(start_angle))
            dy = math.sin(math.radians(start_angle))
            screenX += 1
            raydata = map.ray(self.player.posX, self.player.posY, dx, dy)
            dist = raydata[0] * math.cos(math.radians(abs(player_angle - start_angle)))
            height = wall_height / dist
            screenY = self.display.height / 2 - height / 2

            color_shade = abs(max(1, dist))
            color = (raydata[1][0] / color_shade, raydata[1][1] / color_shade, raydata[1][2] / color_shade)

            if start_angle + 1 > player_angle and start_angle - 1 < player_angle:
                self.min_dist = dist

            print color_shade
            pygame.draw.rect(self.display.renderWindow, color, (screenX, screenY, 1, height), 1)