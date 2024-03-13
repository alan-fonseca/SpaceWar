import random

from SpaceWar.Const import WIN_WIDTH, WIN_HEIGHT
from SpaceWar.code.Background import Background
from SpaceWar.code.Enemy import Enemy
from SpaceWar.code.Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                lista_bg = []
                for i in range(7):
                    lista_bg.append(Background(f'Level1Bg{i}', (0, 0)))  # Gerar o(s) fundo(s) de imagem
                    # Ao final da imagem "passando", gerar uma imagem de continuação
                    lista_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return lista_bg

            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))

            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))

            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(0 + 40, WIN_HEIGHT - 40)))

            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(0 + 40, WIN_HEIGHT - 40)))
