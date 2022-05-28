import pygame
from setup import*
from tile import Tile
from player import Player
class Level:
    def __init__(self):
        #Get Display Surface
        self.display_surface = pygame.display.get_surface()
        #GROUP SETUP (for sprites)
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        #Sprite Initialization
        self.create_map()
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'p':
                    Player((x,y),[self.visible_sprites])
    def run(self):
        #Updates
        self.visible_sprites.draw(self.display_surface)