"""
Diese Klasse bildet die Karte ab. Auf ihr wird festgehalten welcher
Punkt sich an welcher stellt befindet. Um auszumachen welche Punkte gerändert werden und
um neue Punkte hinzuzufügen
"""
import pygame
from PointMap.PointGrid import PointGrid

class PointMap:
  def __init__(self):
    self.screen = pygame.display.get_surface()
    self.window_size = pygame.display.get_window_size()

    # Grid Config
    self.grid_start_x = 0
    self.grid_start_y = 0
    self.cell_size = 100
    self.cells_per_row = 20
    self.rows_per_grid = 20
    self.grid = PointGrid(
      self.grid_start_x,
      self.grid_start_y,
      self.cell_size,
      self.cells_per_row,
      self.rows_per_grid
    )

  def render(self):
    self.grid.render()

  def get_chunk(self, screen_position):
    # screen_position = [ screen_x, screen_y ]
    # TODO: It still has to be implemented that only 
    # chunks are returned that actually exist in 
    # the point map XD. At the moment we just 
    # make sure that there are enough chunks but there is no limit.
    screen_x = screen_position[0] - 150
    screen_y = screen_position[1] - 150
    chunk = []
    screen_size_x = 300
    screen_size_y = 300
    # I will use the screen size for the chunk later
    max_pixel_x = screen_x + screen_size_x
    max_pixel_y = screen_y + screen_size_y

    array_indicies_start_x = int(screen_x / self.cell_size)
    array_indicies_end_x = int(max_pixel_x / self.cell_size);

    if max_pixel_x % self.cell_size != 0:
      array_indicies_end_x += 1;

    array_indicies_start_y = int(screen_y / self.cell_size)
    array_indicies_end_y = int(max_pixel_y / self.cell_size)

    if max_pixel_y % self.cell_size != 0:
      array_indicies_end_y += 1

    # print("Chunk X")
    # print(array_indicies_start_x)
    # print(array_indicies_end_x)

    # print("")

    # print("Chunk Y")
    # print(array_indicies_start_y)
    # print(array_indicies_end_y)
    chunk_coordinates = [
      [array_indicies_start_x, array_indicies_end_x],
      [array_indicies_start_y, array_indicies_end_y],
    ]

    return chunk_coordinates

  def render_chunk(self, chunk_coordinates):
    # chunk_coordinates = [
    #   [index_start_x, index_end_x]
    #   [index_start_y, index_end_y]
    # ]
    x = chunk_coordinates[0]
    y = chunk_coordinates[1]
    # self.grid.grid[0].row[0].render()
    for y_index in range(y[0], y[1]):
      for x_index in range(x[0], x[1]):
        self.grid.grid[y_index].row[x_index].render()


    