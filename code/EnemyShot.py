from SpaceWar.Const import ENTITY_SPEED
from SpaceWar.code.Entity import Entity


class EnemyShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        pass
    #
    # def shoot(self):
    #     return EnemyShot(f'{self.name}Shot')
