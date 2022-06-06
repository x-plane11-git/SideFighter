import pygame
from setup import*
from tile import Tile
from player import Player
from debugfn import debug
from support import*
class Level:
    def __init__(self):
        #Get Display Surface
        self.display_surface = pygame.display.get_surface()
        #GROUP SETUP (for sprites)
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        #Sprite Initializationz
        self.create_map()
    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('../map_data/csv/basemap_Constraints.csv'),
            'structure': import_csv_layout('../map_data/csv/basemap_Structure.csv'),
            'worldone': import_csv_layout('../map_data/csv/basemap_World Objects 1.csv'),
            'worldtwo': import_csv_layout('../map_data/csv/basemap_World Objects 2.csv'),
            'worldthree': import_csv_layout('../map_data/csv/basemap_World Objects 3.csv'),
        }
        graphics = {
                'structure': import_folder('../graphics/structure'),
#                'worldone': import_folder('../graphics/worldone')
                }
        for style,layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1': #1:50:50
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                    if style == 'boundary':
                        Tile((x,y),[self.obstacle_sprites],'invisible')
                    if style == 'structure':
                        surf = graphics['objects'][int(col)]
                        Tile((x,y),[self.obstacle_sprites,self.obstacle_sprites],'object',surf)
                    if style == 'worldone':
                        pass
                    if style == 'worldtwo':
                        pass
                    if style == 'worldthree':
                        pass
#                if col == 'x':
#                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
#                if col == 'p':
#                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
        self.player = Player((1000,1500),[self.visible_sprites],self.obstacle_sprites)
    def run(self):
        #Updates
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.direction)
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        #basic settings
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1]//2
        self.offset = pygame.math.Vector2()
        #creating floor
        self.floor_surf = pygame.image.load('../map_data/basemap.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
    def custom_draw(self,player):
        #getting offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        #draw floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)
        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery): #sorts by a keuy 'metric'
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
        