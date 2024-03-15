import random

from SpaceWar.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from SpaceWar.code.EnemyShot import EnemyShot
from SpaceWar.code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name] + random.randint(0, 100)
            return EnemyShot(f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
