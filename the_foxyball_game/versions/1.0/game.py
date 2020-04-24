import pygame, sys
from random import randint

from players.gracz1 import gracz1
from players.gracz2 import gracz2
from players.bot import bot

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (129, 187, 129)
GRAY = (225, 225, 225)

WIDTH = 720
HEIGHT = 488

class Game(object):

    def __init__(self):
        self.max_fps = 60.0
        pygame.init()
        font = pygame.font.Font('ostrich-regular.ttf', 32)

        #SCREEN
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('The Foxyball Game')
        self.background = pygame.transform.scale(pygame.image.load('textures/background.png'), (WIDTH, HEIGHT))

        #POCZĄTKOWA POZYCJA GRACZA 1:
        self.x_gracz1 = 0
        self.y_gracz1 = 0

        #POCZĄTKOWA POZYCJA GRACZA 2:
        self.x_gracz2 = 200
        self.y_gracz2 = 0

        #PĘTLA
        self.clock = pygame.time.Clock()
        self.czas = 0.0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            self.czas += self.clock.tick()/1000.0
            
            while self.czas > 1/self.max_fps:
                self.czas -= 1/self.max_fps

                #RUCH GRACZY:
                self.poruszanie_gracz1()
                self.poruszanie_gracz2()

                #WYŚWIETLANIE OBECNEJ POZYCJI OBIEKTÓW:
                text = font.render("GRACZ 1: x:%d y:%d GRACZ 2: x:%d y:%d" % (self.x_gracz1, self.y_gracz1, self.x_gracz2, self.y_gracz2), True, WHITE, BLACK)
                textRect = text.get_rect()
                textRect.center = (WIDTH/2, HEIGHT/2)

                #WYŚWIETLANIE OBIEKTÓW:
                self.screen.blit(self.background, (0, 0))
                self.screen.blit(text, textRect)
                self.rysuj()
                pygame.display.flip()

    def poruszanie_gracz1(self):
        klawiatura = pygame.key.get_pressed()
        if klawiatura[pygame.K_d]:
            self.x_gracz1 += 10
        elif klawiatura[pygame.K_a]:
            self.x_gracz1 -= 10
        elif klawiatura[pygame.K_w]:
            self.y_gracz1 -= 10
        elif klawiatura[pygame.K_s]:
            self.y_gracz1 += 10

    def poruszanie_gracz2(self):
        klawiatura = pygame.key.get_pressed()
        if klawiatura[pygame.K_l]:
            self.x_gracz2 += 10
        elif klawiatura[pygame.K_j]:
            self.x_gracz2 -= 10
        elif klawiatura[pygame.K_i]:
            self.y_gracz2 -= 10
        elif klawiatura[pygame.K_k]:
            self.y_gracz2 += 10

    def rysuj(self):
        self.gracz1 = pygame.Rect(self.x_gracz1, self.y_gracz1, 50, 50)
        pygame.draw.rect(self.screen, BLACK, self.gracz1)
        self.gracz2 = pygame.Rect(self.x_gracz2, self.y_gracz2, 50, 50)
        pygame.draw.rect(self.screen, WHITE, self.gracz2)

Game()
