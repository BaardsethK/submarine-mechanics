import pygame
import pygame_menu


class MainMenu:
    pygame.init()
    menu = pygame_menu.Menu("Submarine", 400, 300, theme=pygame_menu.themes.THEME_BLUE)
    menu.add.text_input("Spiller: ", default="Spiller 1")
    menu.add.button('Start spill')
    menu.add.button('Avslutt spill', pygame_menu.events.EXIT)