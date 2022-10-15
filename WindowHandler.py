import pygame
import pygame_menu
from pygame.locals import *

scenes = ["MAIN MENU"]

class WindowHandler:
    def __init__(self):
        self._running= True
        self._display_surf= None
        self._size = self.width, self.height = 640, 400
        self._scene=scenes[0]

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self._size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self._main_menu = pygame_menu.Menu("Submarine", 400, 300, theme=pygame_menu.themes.THEME_BLUE)
        self._main_menu.add.text_input("Spiller: ", default="Spiller 1")
        self._main_menu.add.button('Start spill')
        self._main_menu.add.button('Avslutt spill', pygame_menu.events.EXIT)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        self._main_menu.mainloop(self._display_surf)
        pass
    def on_render(self):
        pass
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running): 
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()

if __name__ == "__main__": 
    window = WindowHandler()
    window.on_execute()