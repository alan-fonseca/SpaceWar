import sys

import pygame as pygame
from pygame import Surface, Rect
from pygame.font import Font

from SpaceWar.Const import WIN_WIDTH, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW
from SpaceWar.Const import COLOR_ORANGE


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./asset/MenuBG.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        menu_option = 0
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(55, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(55, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(25, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 35 * i))
                else:
                    self.menu_text(25, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 35 * i))

            #  Desenhar na tela
            pygame.display.flip()

            #  Verificar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Definindo a saída do jogo (ativando o "X")
                    pygame.quit()  # Encerrando a tela do jogo
                    sys.exit()  # Encerrando o "Sys" para não gerar error (gerar essa tratativa logo no começo)
                if event.type == pygame.KEYDOWN:  # Se alguma tecla foi pressionada
                    if event.key == pygame.K_DOWN:  # Se a tecla "Seta para Baixo" foi pressionada
                        if menu_option >= len(MENU_OPTION) - 1:
                            menu_option = 0
                        else:
                            menu_option += 1

                    if event.key == pygame.K_UP:  # Se a tecla "Seta para Cima" foi pressionada
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
