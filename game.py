import pygame

class Game:
    def __init__(self, name, size, scale):
        pygame.init()
        pygame.display.set_caption(name)

        self.window = pygame.display.set_mode(size, 0, 32)
        self.display = pygame.Surface(self.window.get_width() // scale, self.window.get_height() // scale)

        self.clock = pygame.time.Clock()
