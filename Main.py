import pygame

pygame.init()


class GameMenu():
    def __init__(self, screen, items, bg_color=(192, 192, 192), font=None, font_size=80,
                 font_color=(0, 0, 0)):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
        self.items = items
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color
        self.items = []
        
        for index, item in enumerate(items):
            label = self.font.render(item, 1, font_color)

            width = label.get_rect().width
            height = label.get_rect().height

            positionx = (self.scr_width / 2) - (width / 2)
            # totalheight: total height of text block
            totalheight = len(items) * height
            positiony = (self.scr_height / 2) - (totalheight / 2) + (index * height)

            self.items.append([item, label, (width, height), (positionx, positiony)])

    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False

            # Redraw the background
            self.screen.fill(self.bg_color)

            for name, label, (width, height), (positionx, positiony) in self.items:
                self.screen.blit(label, (positionx, positiony))

            pygame.display.flip()


if __name__ == "__main__":
    # Creating the screen
    screen = pygame.display.set_mode((800, 600), 0, 32)
    menu_items = ('Start', 'Quit')
    pygame.display.set_caption('Hunt the Wumpus')
    gm = GameMenu(screen, menu_items)
    gm.run()