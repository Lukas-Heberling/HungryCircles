"""
Diese Klasse bildet die Karte ab. Auf ihr wird festgehalten welcher
Punkt sich an welcher stellt befindet. Um auszumachen welche Punkte gerändert werden und
um neue Punkte hinzuzufügen
"""
from Blob import Blob
from random import randint

class PointMap:
  def __init__(self, screen):
    self.screen = screen
    self.grid = self.build_grid(0, 0)

  def render(self):
    for row in self.grid:
      for cell in row:
        for element in cell:
          element.render()

  def get_chunk(self, screen_x, screen_y):
    chunk = []
    max_pixel_x = screen_x + 700
    array_indicies_start = int(screen_x / 50)
    array_indicies_end = int(max_pixel_x / 50);
    if max_pixel_x % 50 != 0:
      array_indicies_end += 1;
    print(array_indicies_start)
    print(array_indicies_end)
    pass

  def build_cell(self, start_x, start_y):
    cell = []
    for i in range(0, 3):
      new_x = randint(start_x, start_x + 100)
      new_y = randint(start_y, start_y + 100)
      radius = 10
      color = (randint(0, 255), randint(0, 255), randint(0, 255))
      cell.append(Blob(self.screen, new_x, new_y, radius, color))
    return cell

  def build_row(self, start_x, start_y):
    row = []
    current_x = start_x
    for i in range(0, 20):
      new_cell = self.build_cell(current_x, start_y)
      row.append(new_cell)
      current_x += 100
    return row

  def build_grid(self, start_x, start_y):
    grid = []
    current_y = start_y
    for i in range(0, 20):
      new_row = self.build_row(start_x, current_y)
      grid.append(new_row)
      current_y += 100
    return grid

    