from SpaceWar.Const import WIN_WIDTH
from SpaceWar.code.Background import Background


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
