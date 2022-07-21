import pygame
import sys
from Blob import Blob
from Player import Player
from PointMap import PointMap

class Game:
  def __init__(self):
    # Init pygame
    pygame.init()
    pygame.font.init()

    # Constants
    self.screen_size = (700, 700)

    # Init Screen
    self.screen = pygame.display.set_mode(self.screen_size)
    # Set Caption
    pygame.display.set_caption("Hungry Circles")

    self.player = Player(self.screen, 0, 700, 50, (255, 255, 255), 5)
    self.point_map = PointMap(self.screen)

  def handleEvents(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

  def update(self):
    mouse = pygame.mouse.get_pos()
    mouse_vector = pygame.Vector2(mouse[0], mouse[1])
    self.player.update(mouse_vector)

  def render(self):
    self.screen.fill((0, 0, 0))
    self.point_map.render()
    self.player.render()
    pygame.display.update()