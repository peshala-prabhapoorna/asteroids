import pygame as pg

# Base class for game objects
class CircleShape(pg.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pg.Vector2(x, y)
        self.velocity = pg.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def is_colliding(self, asteroid):
        distance = self.position.distance_to(asteroid.position)

        if distance <= self.radius + asteroid.radius:
            return True
        return False
