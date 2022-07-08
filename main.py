import pygame, sys
from settings import *
#from debug import debug

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Xerdo')
        pygame.display.set_icon(pygame.image.load('graphics/XCON.png').convert_alpha())

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()