'''
Khallid Konnections World
'''

from turtle import position
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
random_generator = random.Random()


app = Ursina()
Sky(texture='sky_sunset')

# Define a Voxel class.
# By setting the parent to scene and the model to 'cube' it becomes a 3d button.

sword = Entity(
    model='blade',
    texture='assests\sword',
    rotation = (30,-40),
    position=(0.5,-0.6),
    parent=scene,
    scale=(0.2,0.15)
)

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'white_cube',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.gold
        )


    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal)

            if key == 'right mouse down':
                destroy(self)

            if key == 'z':
                self.highlight_color = color.red

        if key == 'm':
            self.position = (0,0,0)
            print('Reset Position')


    def updateSword(self, key):
        if key == 'x':
            sword.position = (0.4,-0.5)
        elif key == 'c':
            sword.position = (0.4,-0.5)
        else:
            sword.position = (0.5,-0.6)


for z in range(40):
    for x in range(40):
        voxel = Voxel(position=(x,0,z))


player = FirstPersonController()
app.run()