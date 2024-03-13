import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from SpaceWar.Const import COLOR_WHITE, MENU_OPTION, EVENT_ENEMY
from SpaceWar.code import Entity
from SpaceWar.code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option  # Opção do menu
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))

        # Definindo tempo aleatório para entrada de inimigo no jogo
        pygame.time.set_timer(EVENT_ENEMY, 3500)


    def run(self, ):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()  # Instanciando objeto da classe Clock, objetivo de controlar velocidade do jogo
        while True:
            clock.tick(60)  # Define quantos quadros por segundo durante o "for"
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # Aqui é desenhado a Entidade (background, jogador 1)
                self.level_text(20, f'fps: {clock.get_fps(): .0f}', COLOR_WHITE, (10, 10))
                # print(clock.get_fps())
                ent.move()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:  # Definindo a saída do jogo (ativando o "X")
                    pygame.quit()  # Encerrando a tela do jogo
                    sys.exit()  # Encerrando o "Sys" para não gerar error (gerar essa tratativa logo no começo)

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity('Enemy1'))

            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
