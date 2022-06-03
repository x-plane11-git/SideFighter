import pygame
from setup import*
class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        
        self.direction = pygame.math.Vector2() #x,y vector (0,0) to change direction
        self.speed = 3
        
        self.obstacle_sprites = obstacle_sprites
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
     
    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.x += self.direction.x * speed
        #self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        #self.collision('vertical')
        #self.rect.center += self.direction * speed
    '''
    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: #moving to the right
                        self.rect.right = sprite.rect.left #if player moves right, collides with obstacle, right side of player is moved to left side of object
                    if self.direction.y < 0: #player moves left
                        self.rect.left = sprite.rect.right
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: #downwards movement
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: #upwards movement
                        self.rect.top = sprite.rect.bottom
    '''
    def update(self):
        self.input()
        self.move(self.speed)