import pygame
import sys
from Game import Game

def game_loop():
  game = Game()
  clock = pygame.time.Clock()
  while 1:
    game.handleEvents()
    game.update()
    game.render()
    clock.tick(60)

game_loop()