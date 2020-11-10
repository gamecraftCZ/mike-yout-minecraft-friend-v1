from typing import List

import numpy as np
import vpython
from vpython import vector as v

from constants import WORLD_SHAPE
from game import Player, Game


BLOCK_COLORS = {1: v(0.9, 0.7, 0.5), 2: v(0.8, 0.8, 0.4), 3: vpython.color.green}

class Renderer:
    blocks: List[List[List[vpython.box]]] = []
    player: vpython.cylinder

    def render_blocks(self, game: Game):
        for z in range(game.environment.shape[0]):
            for y in range(game.environment.shape[1]):
                for x in range(game.environment.shape[2]):
                    block = game.environment[z][y][x]
                    old = self.blocks[z][y][x]
                    if block:
                        color = BLOCK_COLORS[block]

                        if old and old.color != color:
                            old.color = color
                        else:
                            obj = vpython.box(pos=v(y + 0.5, z + 0.5, x + 0.5), size=v(1, 1, 1), color=color)
                            self.blocks[z][y][x] = obj
                    elif old:
                        old.delete()


    def render_player(self, game: Game):
        position = game.player.position
        print(position.z)
        self.player.pos = v(position.y, position.z, position.x)


    def render(self, game: Game):
        self.render_blocks(game)
        self.render_player(game)
        print("Rendered")

    def __init__(self):
        self.canvas = vpython.canvas(title="Be more of who you are!", width=800, height=800)
        self.canvas.center = v(WORLD_SHAPE.y / 2, 0, WORLD_SHAPE.x / 2)  # Camera to rotate around real center

        self.player = vpython.cylinder(axis=v(0, 1.8, 0), up=v(0, 0, 1), radius=0.3, color=vpython.color.red)

        self.blocks = []
        for z in range(WORLD_SHAPE.z):
            self.blocks.append([])
            for y in range(WORLD_SHAPE.y):
                self.blocks[z].append([])
                for x in range(WORLD_SHAPE.x):
                    self.blocks[z][y].append(None)

        print("Initialized Renderer")
