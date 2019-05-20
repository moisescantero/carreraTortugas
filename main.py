import pygame
from pygame.locals import *
import sys

class Race():
    def __init__(self, width, height):
        self.size = (width, height)
        self.title = "Carrera automática"
        
        self.background = pygame.image.load("assets/background.png")
    
    def launch(self):
        pygame.font.init()
        pygame.init()
        self.screen = pygame.display.set_mode(self.__size, pygame.HWSURE)
        pygame.display.set_caption(self.__title)
        
        winner = False
        
        while not winner:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()