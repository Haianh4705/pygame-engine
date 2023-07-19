import pygame, sys

class Game:
    def __init__(self, name, size, scale):
        pygame.init()
        pygame.display.set_caption(name)

        self.name = name
        self.size = size
        self.scale = scale

        self.window = pygame.display.set_mode(self.size, 0, 32)
        self.display = pygame.Surface(self.window.get_width() // self.scale, self.window.get_height() // self.scale)

        self.clock = pygame.time.Clock()
    
    def run(self, fps=60, bg=(0, 0, 0)):
        while True:
            dt = self.clock.tick(fps) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.display.fill(bg)
            self.window.blit(pygame.transform.scale(self.display, self.window.get_size()), (0, 0))
            
            pygame.display.update()
