import random
import pygame
import pygame_menu
from pygame.locals import *
from PlayerHandler import Player

scenes = ["MAIN MENU"]
player_keys = {
    "keys_1" : [K_UP, K_DOWN,K_LEFT,K_RIGHT],
    "keys_2" : [K_w,K_s,K_a,K_d]
}
player_colors = {
    "blue" : (0, 0, 255),
    "red" : (255, 0, 0)
}

class WindowHandler:
    def __init__(self):
        self._running= True
        self._display_surf= None
        self._size = self.width, self.height = 640, 400
        self._scene = scenes[0]
        self._clock = pygame.time.Clock()
        self._active_players = []
        self._all_sprites = pygame.sprite.Group()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self._size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self._main_menu = pygame_menu.Menu("Submarine", 400, 300, theme=pygame_menu.themes.THEME_BLUE)
        self._main_menu.add.text_input("Spiller: ", default="Spiller 1")
        self._main_menu.add.button('Start spill', )
        self._main_menu.add.button('Avslutt spill', pygame_menu.events.EXIT)
        self.player1 = Player("Player 1",player_keys["keys_1"], player_colors["blue"],self.width,self.height)
        self.player2 = Player("Player 2",player_keys["keys_2"], player_colors["red"], self.width,self.height)
        self._active_players.append(self.player1)
        self._active_players.append(self.player2)
        self._all_sprites.add(self._active_players)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        #self._main_menu.mainloop(self._display_surf)
        self._pressed_keys = pygame.key.get_pressed()
        pass

    def on_render(self):
        for sprite in self._all_sprites:
            self._display_surf.blit(sprite.surf,sprite.rect)
        for player in self._active_players:
            player.move_player(self._pressed_keys)

        pygame.display.flip()
        self._clock.tick(60)
        self._display_surf.fill((0,0,0)) #"deletes the old frame by painting it black"

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