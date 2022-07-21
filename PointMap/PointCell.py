"""
A cell is an area that is filled with points that the circles can then later eat
"""
from random import randint
from Blob import Blob

class PointCell:
  def __init__(self, start_x, start_y, cell_size):
    self.cell = []
    self.point_radius = 10

    for i in range(0, 3):
      # Creating a random position for the point in the cell
      new_x = randint(start_x, start_x + cell_size)
      new_y = randint(start_y, start_y + cell_size)
      color = (randint(0, 255), randint(0, 255), randint(0, 255))
      self.cell.append(
        Blob(
          new_x,
          new_y,
          self.point_radius,
          color
        )
      )
  
  def render(self):
    for point in self.cell:
      point.render()

