"""
Die Entity klasse ist die Basisklasse für alle
Elemente im Spiel
"""
import pygame

class Entity:
  def __init__(self, pos_x, pos_y):
    self.pos = pygame.Vector2(
      pos_x if pos_x else 0,
      pos_y if pos_y else 0
    )

  def set_x(self, pos_x):
    self.pos.x = pos_x
  
  def set_y(self, pos_y):
    self.pos.y = pos_y

  def set_xy(self, pos_x , pos_y):
    self.pos.update(pos_x, pos_y)