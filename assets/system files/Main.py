import pygame, sys
from setup import*
from level import Level
from pyvidplayer import Video
def intro(): #intro video function
    vid = Video("../graphics/media/intro.mp4")
    vid.set_size((WIDTH,HEIGHT))
    while True:
        screen = pygame.display.set_mode((WIDTH,HEIGHT))
        vid.draw(screen, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                torun()
def torun(): #main game class and functions
    class Game:
        def __init__(self):
            #initialization
            pygame.init()
            self.screen = pygame.display.set_mode((WIDTH,HEIGHT))#,pygame.FULLSCREEN)
            pygame.display.set_caption('Velocious Brawlers')
            self.clock = pygame.time.Clock()
            self.level = Level()
    
        def run(self): #drawing into pygame window
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
            
                self.screen.fill('black')
                self.level.run()
                pygame.display.update()
                self.clock.tick(FPS)
    if __name__ == '__main__': #check if it is main file
        game = Game() #Create instance
        game.run() #run class
intro() #call the intro function