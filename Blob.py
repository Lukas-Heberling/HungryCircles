""" 
Ein Blob ist die Basisklasse für den Spieler und die Gegner und Erbt
von Entity. Mir ist kein Besserer Name eingefallen deswegen heißt diese klasse fürs
Erste einfach mal Blob
"""
import pygame
from Entity import Entity

class Blob(Entity):
  def __init__(self, pos_x , pos_y, start_radius, color):
    super().__init__(pos_x, pos_y)
    self.radius = start_radius
    self.screen = pygame.display.get_surface()
    self.color = color

  def set_width(self, new_width):
    self.width = new_width

  def update_width(self, update_width):
    self.width += update_width

  def render(self):
    pygame.draw.circle(
      self.screen,
      self.color,
      self.pos,
      self.radius
    )