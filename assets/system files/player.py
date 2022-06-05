import pygame
from setup import*
class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-20)
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
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center
        #1:06:00
    def collision(self,direction):
        if direction == 'horizontal':
           
            for sprite in self.obstacle_sprites:
##                print(self.rect,self.direction) <debugging
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: #moving to the right
                        self.hitbox.right = sprite.hitbox.left #if player moves right, collides with obstacle, right side of player is moved to left side of object
                    if self.direction.x < 0: #player moves left
                        self.hitbox.left = sprite.hitbox.right
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: #downwards movement
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: #upwards movement
                        self.hitbox.top = sprite.hitbox.bottom
    
    def update(self):
        self.input()
        self.move(self.speed)
