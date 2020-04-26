import pygame, sys
from random import randint
from random import randrange

from players.gracz1 import gracz1
from players.gracz2 import gracz2
from players.bot import bot
from menu import game_menu

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (129, 187, 129)
GRAY = (205, 205, 205)
RED = (255, 0, 0)

#DEFAULT RESOLUTION
#WIDTH = 720
#HEIGHT = 480

WIDTH = 1280
HEIGHT = 720

class Game(object):

    def __init__(self, punkty_graczy):
        #FIZYKA
        self.g = 9.81
        self.dt = 0.2

        #PODSTAWOWE FUNKCJE
        self.max_fps = 60.0
        pygame.init()
        font = pygame.font.Font('ostrich-regular.ttf', 32)

        #SCREEN
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption('The Foxyball Game')
        self.background = pygame.transform.scale(pygame.image.load('textures/background.png'), (WIDTH, HEIGHT))

        #WIELKOSC GRACZY
        self.szerokosc_graczy = 100
        self.wysokosc_graczy = 50

        #ZAPIS KLAWISZY
        self.keys1 = [0,0,0,0] #[W,S,A,D]
        self.keys2 = [0,0,0,0]  # [I,K,J,L]

        #LICZBA PUNKTÓW
        self.punkty_graczy = punkty_graczy
        self.punkty_gracz1 = self.punkty_graczy[0]
        self.punkty_gracz2 = self.punkty_graczy[1]

        #INICJACJA ELEMENTÓW     
        #LICZBA ODBIĆ
        self.odbicia = 0
        self.odbicia2 = 0

        #PLANSZA
        self.podloga = pygame.Rect(0, 0, 0, 0)
        self.sufit = pygame.Rect(0, 0, 0, 0)
        self.lewa_ramka = pygame.Rect(0, 0, 0, 0)
        self.prawa_ramka = pygame.Rect(0, 0, 0, 0)
        self.srodek = pygame.Rect(0, 0, 0, 0)
        #PILKA
        self.pilka = pygame.Rect(0, 0, 0, 0)
        #GRACZ 1
        self.gracz1 = pygame.Rect(0, 0, 0, 0)
        self.hitbox_gracz1_lewy = pygame.Rect(0, 0, 0, 0)
        self.hitbox_gracz1_prawy = pygame.Rect(0, 0, 0, 0)
        self.hitbox_gracz1_gorny = pygame.Rect(0, 0, 0, 0)
        self.hitbox_gracz1_dolny = pygame.Rect(0, 0, 0, 0)
        #GRACZ2
        self.gracz2 = pygame.Rect(0, 0, 0, 0)
        self.hitbox_gracz2_lewy = pygame.Rect(0, 0, 0, 0)
        self.hitbox_gracz2_prawy = pygame.Rect(0, 0, 0, 0)
        self.hitbox_gracz2_gorny = pygame.Rect(0, 0, 0, 0)
        self.hitbox_gracz2_dolny = pygame.Rect(0, 0, 0, 0)
        #SIATKA
        self.siatka = pygame.Rect(0, 0, 0, 0)
        self.hitbox_siatka_lewy = pygame.Rect(0, 0, 0, 0)
        self.hitbox_siatka_prawy = pygame.Rect(0, 0, 0, 0)
        self.hitbox_siatka_gorny = pygame.Rect(0, 0, 0, 0)
        self.hitbox_siatka_dolny = pygame.Rect(0, 0, 0, 0)
        #POCZĄTKOWA POZYCJA I SZYBKOSC GRACZA 1:
        self.x_gracz1 = 0.2*WIDTH
        self.y_gracz1 = 0.8*HEIGHT
        self.dx_gracz1 = 0
        self.dy_gracz1 = 0
        self.lot_gracz1 = 0
        #POCZĄTKOWA POZYCJA I SZYBKOSC GRACZA 2:
        self.x_gracz2 = 0.8*WIDTH
        self.y_gracz2 = 0.8*HEIGHT
        self.dx_gracz2 = 0
        self.dy_gracz2 = 0
        self.lot_gracz2 = 0
        #POZYCJA SIATKI:
        self.szerokosc_siatki = WIDTH*0.05
        self.wysokosc_siatki = HEIGHT*0.45
        self.x_siatki = (WIDTH-self.szerokosc_siatki)/2
        self.y_siatki = (HEIGHT*0.8-self.wysokosc_siatki+self.wysokosc_graczy)
        #PIŁKA:
        self.promien_pilki = 25
        self.x_pilki = 0.5*WIDTH-self.promien_pilki
        self.y_pilki = 0.2*HEIGHT
        self.dx_pilki = 0
        while self.dx_pilki == 0:
            self.dx_pilki = randrange(-10, 10)
        self.dx_pilki /= 10
        self.dy_pilki = randrange(-20, -10)

        #PĘTLA
        self.clock = pygame.time.Clock()
        self.czas = 0.0
        self.foxygame = True
        while self.foxygame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            #self.czas += self.clock.tick()/1000.0
            #while self.czas > 1/self.max_fps:
                #self.czas -= 1/self.max_fps

            #RUCH GRACZY:
            self.odczyt_klawiszy_gracz1()
            self.odczyt_klawiszy_gracz2()
            self.ruch()
            self.ruch_pilki()
            #WYŚWIETLANIE OBECNEJ POZYCJI OBIEKTÓW:
            text = font.render("%d///%d///%f////GRACZ 1: x:%d y:%d GRACZ 2: x:%d y:%d" % (self.punkty_graczy[0], self.punkty_graczy[1], self.dx_pilki,self.x_gracz1, self.y_gracz1, self.x_gracz2, self.y_gracz2), True, WHITE, BLACK)
            textRect = text.get_rect()
            textRect.center = (WIDTH/2, HEIGHT/6)
            text2 = font.render("CZAS: %f///ODBICIA %d///%d///GRACZ 1: a:%d d:%d GRACZ 2: j:%d l:%d" % (self.czas, self.odbicia, self.odbicia2, self.keys1[2], self.keys1[3], self.keys2[2], self.keys2[3]), True, WHITE, BLACK)
            textRect2 = text2.get_rect()
            textRect2.center = (WIDTH/2, HEIGHT/10)
            #WYŚWIETLANIE OBIEKTÓW:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(text, textRect)
            self.screen.blit(text2, textRect2)
            self.rysuj()
            self.clock.tick(60)
            pygame.display.flip()
        self.zwroc_wynik()

    def odczyt_klawiszy_gracz1(self):
        klawiatura = pygame.key.get_pressed()
        if klawiatura[pygame.K_d] and not pygame.Rect.colliderect(self.hitbox_siatka_lewy, self.gracz1):
            self.keys1[3] = 1
        else:
            self.keys1[3] = 0

        if klawiatura[pygame.K_a] and not pygame.Rect.colliderect(self.lewa_ramka, self.gracz1):
            self.keys1[2] = 1
        else:
            self.keys1[2] = 0

        if klawiatura[pygame.K_w] and not self.lot_gracz1:
            self.keys1[0] = 1
            self.lot_gracz1 = 1
            self.dy_gracz1 = -60
        else:
            self.keys1[0] = 0
        #elif klawiatura[pygame.K_s]:
            #self.y_gracz1 += self.dy

    def odczyt_klawiszy_gracz2(self):
        klawiatura = pygame.key.get_pressed()
        if klawiatura[pygame.K_l] and not pygame.Rect.colliderect(self.prawa_ramka, self.gracz2):
            self.keys2[3] = 1
        else:
            self.keys2[3] = 0
            
        if klawiatura[pygame.K_j] and not pygame.Rect.colliderect(self.hitbox_siatka_prawy, self.gracz2):
            self.keys2[2] = 1
        else:
            self.keys2[2] = 0
        
        if klawiatura[pygame.K_i] and not self.lot_gracz2:
            self.keys2[0] = 1
            self.lot_gracz2 = 1
            self.dy_gracz2 = -60
        else:
            self.keys2[0] = 0
       # elif klawiatura[pygame.K_i]:
            #self.y_gracz2 -= self.dy
        #elif klawiatura[pygame.K_k]:
            #self.y_gracz2 += self.dy

    def rysuj(self):
        #PODŁOGA
        self.podloga = pygame.Rect(0, 0.8*HEIGHT+self.wysokosc_graczy, WIDTH, 1)
        pygame.draw.rect(self.screen, RED, self.podloga)
        #LEWA RAMKA
        self.lewa_ramka = pygame.Rect(0, 0, 1, HEIGHT)
        pygame.draw.rect(self.screen, RED, self.lewa_ramka)
        #PRAWA RAMKA
        self.prawa_ramka = pygame.Rect(WIDTH-1, 0, 1, HEIGHT)
        pygame.draw.rect(self.screen, RED, self.prawa_ramka)
        #SUFIT
        self.sufit = pygame.Rect(0, 0, WIDTH, 1)
        pygame.draw.rect(self.screen, RED, self.sufit)
        #ŚRODEK
        self.srodek = pygame.Rect(self.x_siatki+(self.szerokosc_siatki/2), 0, 1, HEIGHT)
        pygame.draw.rect(self.screen, RED, self.srodek)

        #SIATKA
        self.siatka = pygame.Rect(self.x_siatki, self.y_siatki, self.szerokosc_siatki, self.wysokosc_siatki)
        pygame.draw.rect(self.screen, GRAY, self.siatka)
        self.hitbox_siatka_lewy = pygame.Rect(self.x_siatki, self.y_siatki, 1, self.wysokosc_siatki)
        self.hitbox_siatka_prawy = pygame.Rect(self.x_siatki+self.szerokosc_siatki, self.y_siatki, 1, self.wysokosc_siatki)
        self.hitbox_siatka_gorny = pygame.Rect(self.x_siatki, self.y_siatki, self.szerokosc_siatki, 1)
        self.hitbox_siatka_dolny = pygame.Rect(self.x_siatki, self.y_siatki+self.wysokosc_siatki, self.szerokosc_siatki, 1)
        pygame.draw.rect(self.screen, RED, self.hitbox_siatka_lewy)
        pygame.draw.rect(self.screen, RED, self.hitbox_siatka_prawy)
        pygame.draw.rect(self.screen, RED, self.hitbox_siatka_gorny)
        pygame.draw.rect(self.screen, RED, self.hitbox_siatka_dolny)

        #GRACZ 1
        self.gracz1 = pygame.Rect(self.x_gracz1, self.y_gracz1, self.szerokosc_graczy, self.wysokosc_graczy)
        pygame.draw.rect(self.screen, BLACK, self.gracz1)
        self.hitbox_gracz1_lewy = pygame.Rect(self.x_gracz1, self.y_gracz1, 1, self.wysokosc_graczy)
        self.hitbox_gracz1_prawy = pygame.Rect(self.x_gracz1+self.szerokosc_graczy, self.y_gracz1, 1, self.wysokosc_graczy)
        self.hitbox_gracz1_gorny = pygame.Rect(self.x_gracz1, self.y_gracz1, self.szerokosc_graczy, 1)
        self.hitbox_gracz1_dolny = pygame.Rect(self.x_gracz1, self.y_gracz1+self.wysokosc_graczy, self.szerokosc_graczy, 1)
        pygame.draw.rect(self.screen, RED, self.hitbox_gracz1_lewy)
        pygame.draw.rect(self.screen, RED, self.hitbox_gracz1_prawy)
        pygame.draw.rect(self.screen, RED, self.hitbox_gracz1_gorny)
        pygame.draw.rect(self.screen, RED, self.hitbox_gracz1_dolny)

        #GRACZ 2
        self.gracz2 = pygame.Rect(self.x_gracz2, self.y_gracz2, self.szerokosc_graczy, self.wysokosc_graczy)
        pygame.draw.rect(self.screen, WHITE, self.gracz2)
        self.hitbox_gracz2_lewy = pygame.Rect(self.x_gracz2, self.y_gracz2, 1, self.wysokosc_graczy)
        self.hitbox_gracz2_prawy = pygame.Rect(self.x_gracz2+self.szerokosc_graczy, self.y_gracz2, 1, self.wysokosc_graczy)
        self.hitbox_gracz2_gorny = pygame.Rect(self.x_gracz2, self.y_gracz2, self.szerokosc_graczy, 1)
        self.hitbox_gracz2_dolny = pygame.Rect(self.x_gracz2, self.y_gracz2+self.wysokosc_graczy, self.szerokosc_graczy, 1)
        pygame.draw.rect(self.screen, RED, self.hitbox_gracz2_lewy)
        pygame.draw.rect(self.screen, RED, self.hitbox_gracz2_prawy)
        pygame.draw.rect(self.screen, RED, self.hitbox_gracz2_gorny)
        pygame.draw.rect(self.screen, RED, self.hitbox_gracz2_dolny)

        #PIŁKA
        self.pilka = pygame.Rect(self.x_pilki, self.y_pilki, 2*self.promien_pilki, 2*self.promien_pilki)
        pygame.draw.rect(self.screen, RED, self.pilka)
        #pygame.draw.circle(self.screen, GREEN, self.pozycja_pilki, self.promien_pilki)

    def ruch(self):
        #RUCH GRACZA1:
        self.dx_gracz1 = 0
        if self.keys1[2]:
            self.dx_gracz1 -= 40
        if self.keys1[3]:
            self.dx_gracz1 += 40

        if self.lot_gracz1:
            self.dy_gracz1 = self.dy_gracz1 + self.g * self.dt
            self.y_gracz1 = self.y_gracz1 + self.dy_gracz1 * self.dt
        
        if self.lot_gracz1 and pygame.Rect.colliderect(self.podloga, self.gracz1):
            self.dy_gracz1 = 0
            self.lot_gracz1 = 0
            self.y_gracz1 = 0.8*HEIGHT

        self.x_gracz1 += self.dx_gracz1 * self.dt
        #self.y_gracz1 += self.dy_gracz1

        #RUCH GRACZA2:
        self.dx_gracz2 = 0
        if self.keys2[2]:
            self.dx_gracz2 -= 40
        if self.keys2[3]:
            self.dx_gracz2 += 40

        if self.lot_gracz2:
            self.dy_gracz2 = self.dy_gracz2 + self.g * self.dt
            self.y_gracz2 = self.y_gracz2 + self.dy_gracz2 * self.dt

        if self.lot_gracz2 and pygame.Rect.colliderect(self.podloga, self.gracz2):
            self.dy_gracz2 = 0
            self.lot_gracz2 = 0
            self.y_gracz2 = 0.8*HEIGHT

        self.x_gracz2 += self.dx_gracz2 * self.dt
        #self.y_gracz2 += self.dy_gracz2

    def ruch_pilki(self):
        #JESLI PRZEJDZIE NA DRUGA STRONE
        if pygame.Rect.colliderect(self.srodek, self.pilka):
            self.odbicia = 0
            self.odbicia2 = 0
        #JESLI ODBIJE SIE OD PODLOGI
        if pygame.Rect.colliderect(self.podloga, self.pilka) and self.x_pilki+self.promien_pilki<self.x_siatki+(self.szerokosc_siatki/2):
            self.dy_pilki = -60
            self.foxygame = False
            self.punkty_gracz2 += 1
        if pygame.Rect.colliderect(self.podloga, self.pilka) and self.x_pilki+self.promien_pilki>self.x_siatki+(self.szerokosc_siatki/2):
            self.dy_pilki = -60
            self.foxygame = False
            self.punkty_gracz1 += 1
        #JESLI GRACZ ODBIJE JA PONAD 3 RAZY
        if self.odbicia >= 4:
            self.foxygame = False
            self.punkty_gracz2 += 1
        if self.odbicia2 >= 4:
            self.foxygame = False
            self.punkty_gracz1 += 1
        #JESLI ODBIJE SIE OD SUFITU
        if pygame.Rect.colliderect(self.sufit, self.pilka):
            self.dy_pilki *= -1
        #JESLI DOTKNIE LEWEJ LUB PRAWEJ STRONY SIATKI/PLANSZY
        if pygame.Rect.colliderect(self.lewa_ramka, self.pilka) or pygame.Rect.colliderect(self.prawa_ramka, self.pilka) or pygame.Rect.colliderect(self.hitbox_siatka_prawy, self.pilka) or pygame.Rect.colliderect(self.hitbox_siatka_lewy, self.pilka):
            self.dx_pilki *= -1
        #JESLI DOTKNIE GORY SIATKI
        if pygame.Rect.colliderect(self.hitbox_siatka_gorny, self.pilka):
            if self.dx_pilki < 0:
                self.dx_pilki = -(self.x_siatki+(self.szerokosc_siatki/2)-(self.x_pilki+self.promien_pilki))/(self.szerokosc_siatki/2)
            elif self.dx_pilki > 0:
                self.dx_pilki = -(self.x_siatki+(self.szerokosc_siatki/2)-(self.x_pilki+self.promien_pilki))/(self.szerokosc_siatki/2)
            else:
                while self.dx_pilki == 0:
                    self.dx_pilki = randrange(-10, 10)
                    self.dx_pilki /= 10
            self.dy_pilki = -40
        #JESLI GRACZ 1 JA DOTKNIE:
        if pygame.Rect.colliderect(self.hitbox_gracz1_gorny, self.pilka) and not pygame.Rect.colliderect(self.hitbox_gracz1_dolny, self.pilka):
            gracz_a_pilka = (self.x_gracz1+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))
            if gracz_a_pilka < 0:
                self.dx_pilki = -(self.x_gracz1+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))/(self.szerokosc_graczy/2)*5
            else:
                self.dx_pilki = -(self.x_gracz1+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))/(self.szerokosc_graczy/2)*5
        #JESLI GRACZ 2 JA DOTKNIE:
        if pygame.Rect.colliderect(self.hitbox_gracz2_gorny, self.pilka) and not pygame.Rect.colliderect(self.hitbox_gracz2_dolny, self.pilka):
            gracz_a_pilka2 = (self.x_gracz2+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))
            if gracz_a_pilka2 < 0:
                self.dx_pilki = -(self.x_gracz2+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))/(self.szerokosc_graczy/2)*5
            else:
                self.dx_pilki = -(self.x_gracz2+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))/(self.szerokosc_graczy/2)*5
        #JESLI GRACZ 1 UDERZA PILKE
        if pygame.Rect.colliderect(self.hitbox_gracz1_gorny, self.pilka) and self.y_pilki<=self.y_gracz1:
            self.dy_pilki = -80
            self.y_pilki = self.y_gracz1 - self.promien_pilki*2
            self.odbicia += 1
        elif pygame.Rect.colliderect(self.hitbox_gracz1_dolny, self.pilka) and self.y_pilki>self.y_gracz1:
            self.dy_pilki = 80
            self.y_pilki = self.y_gracz1 + self.promien_pilki*2
        #JESLI GRACZ 2 UDERZA PILKE
        if pygame.Rect.colliderect(self.hitbox_gracz2_gorny, self.pilka) and self.y_pilki<=self.y_gracz2:
            self.dy_pilki = -80
            self.y_pilki = self.y_gracz2 - self.promien_pilki*2
            self.odbicia2 += 1
        elif pygame.Rect.colliderect(self.hitbox_gracz2_dolny, self.pilka) and self.y_pilki>self.y_gracz2:
            self.dy_pilki = 80
            self.y_pilki = self.y_gracz2 + self.promien_pilki*2

        self.dy_pilki = self.dy_pilki + self.g * self.dt
        self.y_pilki = self.y_pilki + self.dy_pilki * self.dt
        self.x_pilki += self.dx_pilki

        #self.pozycja_pilki = (int(self.x_pilki+self.promien_pilki), int(self.y_pilki+self.promien_pilki))
    
    def zwroc_wynik(self):
        return [self.punkty_gracz1, self.punkty_gracz2]

gameplay = True
punkty_gracz1 = 0
punkty_gracz2 = 0
punkty_graczy = [punkty_gracz1, punkty_gracz2]
while gameplay:
    punkty_graczy = Game(punkty_graczy).zwroc_wynik()
    print("Obecny wynik: {}/{}".format(punkty_graczy[0], punkty_graczy[1]))
    if punkty_graczy[0] == 5:
        print("Gracz 1 WYGRAŁ!")
        gameplay = False
    elif punkty_graczy[1] == 5:
        print("Gracz 2 WYGRAŁ!")
        gameplay = False

