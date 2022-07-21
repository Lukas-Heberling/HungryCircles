import pygame
import sys
from Player import Player
from PointMap.PointMap import PointMap

class Game:
  def __init__(self):
    # Init pygame
    pygame.init()
    pygame.font.init()

    # Constants
    self.screen_size = (800, 800)

    # Init Screen
    self.screen = pygame.display.set_mode(self.screen_size)
    # Set Caption
    pygame.display.set_caption("Hungry Circles")

    self.player = Player(350, 350, 20, (255, 255, 255), 5)
    self.point_map = PointMap()

  def handleEvents(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

  def update(self):
    # Getting the mouse Position
    mouse_vector = pygame.Vector2(pygame.mouse.get_pos())
    self.player.update(mouse_vector)

  def render(self):
    # Painting the whole screen black
    self.screen.fill((0, 0, 0))
    # Rendering the chunk around the point map
    self.point_map.render_chunk(
      self.point_map.get_chunk(self.player.pos)
    )
    self.player.render()
    pygame.display.update()