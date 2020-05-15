#IMPORT STANDARDOWYCH BIBLIOTEK:
import pygame, sys
from random import randint
from random import randrange
from os import system
system('clear')
#IMPORT WLASNYCH:
from players.gracz1 import gracz1
from players.gracz2 import gracz2
from players.bot import bot
from menu.game_menu import menu
from settings.settings import settings
from static_objects.static import static
from ball.ball import pilka

max_liczba_punktow = settings().max_liczba_punktow

WIDTH = settings().WIDTH
HEIGHT = settings().HEIGHT
BLACK = settings().BLACK
WHITE = settings().WHITE
GREEN = settings().GREEN
GRAY = settings().GRAY
RED = settings().RED

pygame.init()
music = pygame.mixer.music.load('music/background_music.mp3')
pygame.mixer.music.play(-1)
font = pygame.font.Font('fonts/ostrich-regular.ttf', 32)

class Game(object):

    def __init__(self, punkty_graczy):
        #FIZYKA I MAXFPS
        self.g = settings().g
        self.dt = settings().dt
        self.max_fps = settings().max_fps
        self.max_dozwolonych_odbic = settings().max_dozwolonych_odbic
        #self.max_liczba_punktow = settings().max_liczba_punktow
        self.wysokosc_odbicia_pilki_przez_gracza = settings().wysokosc_odbicia_pilki_przez_gracza
        self.wysokosc_odbicia_pilki_od_siatki = settings().wysokosc_odbicia_pilki_od_siatki
        self.szybkosc_pilki_x = settings().szybkosc_pilki_x

        #SCREEN
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption('The Foxyball Game')
        self.background = pygame.transform.scale(pygame.image.load('textures/background.png'), (WIDTH, HEIGHT))

        #WIELKOSC GRACZY
        self.szerokosc_graczy = settings().szerokosc_graczy
        self.wysokosc_graczy = settings().wysokosc_graczy

        #LICZBA PUNKTÓW
        self.punkty_graczy = punkty_graczy
        self.punkty_gracz1 = self.punkty_graczy[0]
        self.punkty_gracz2 = self.punkty_graczy[1]

        #INICJACJA ELEMENTÓW
        #PLANSZA
        self.podloga = static().podloga
        self.sufit = static().sufit
        self.lewa_ramka = static().lewa_ramka
        self.prawa_ramka = static().prawa_ramka
        self.srodek = static().srodek
        #PILKA
        self.pilka = pygame.Rect(0, 0, 0, 0)
        #GRACZ 1
        self.gracz1 = gracz1()
        #GRACZ2
        self.gracz2 = gracz2()
        #SIATKA
        self.siatka = static().siatka
        self.hitbox_siatka_lewy = static().hitbox_siatka_lewy
        self.hitbox_siatka_prawy = static().hitbox_siatka_prawy
        self.hitbox_siatka_gorny = static().hitbox_siatka_gorny
        self.hitbox_siatka_dolny = static().hitbox_siatka_dolny
        #POZYCJA SIATKI:
        self.szerokosc_siatki = static().szerokosc_siatki
        self.wysokosc_siatki = static().wysokosc_siatki
        self.x_siatki = static().x_siatki
        self.y_siatki = static().y_siatki
        #PIŁKA:
        #self.pilka = pilka()
        #LICZBA ODBIĆ
        self.odbicia = 0
        self.odbicia2 = 0
        #self.odbicia = self.pilka.odbicia
        #self.odbicia2 = self.pilka.odbicia2
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
        self.foxygame = settings().foxygame
        while self.foxygame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            #RUCH GRACZY:
            self.gracz1.odczyt_klawiszy()
            self.gracz2.odczyt_klawiszy()
            self.gracz1.ruch()
            self.gracz2.ruch()
            #self.pilka.ruch()
            self.ruch_pilki()
            #WYŚWIETLANIE OBECNEJ POZYCJI OBIEKTÓW:
            text = font.render("PUNKTY GRACZ 1: %d  |  PUNKTY GRACZ 2: %d" % (self.punkty_graczy[0], self.punkty_graczy[1]), True, WHITE, BLACK)
            textRect = text.get_rect()
            textRect.center = (WIDTH/2, HEIGHT/6)
            text2 = font.render("ODBICIA GRACZ 1: %d  |  ODBICIA GRACZ 2: %d" % (self.odbicia, self.odbicia2), True, WHITE, BLACK)
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

    def rysuj(self):
        #PODŁOGA:
        pygame.draw.rect(self.screen, RED, self.podloga)
        #LEWA RAMKA:
        pygame.draw.rect(self.screen, RED, self.lewa_ramka)
        #PRAWA RAMKA:
        pygame.draw.rect(self.screen, RED, self.prawa_ramka)
        #SUFIT:
        pygame.draw.rect(self.screen, RED, self.sufit)
        #ŚRODEK:
        pygame.draw.rect(self.screen, RED, self.srodek)
        #SIATKA:
        pygame.draw.rect(self.screen, GRAY, self.siatka)
        #HITBOXY SIATKI:
        pygame.draw.rect(self.screen, RED, self.hitbox_siatka_lewy)
        pygame.draw.rect(self.screen, RED, self.hitbox_siatka_prawy)
        pygame.draw.rect(self.screen, RED, self.hitbox_siatka_gorny)
        pygame.draw.rect(self.screen, RED, self.hitbox_siatka_dolny)

        #GRACZ 1
        self.gracz1.gr1 = pygame.Rect(self.gracz1.x, self.gracz1.y, self.szerokosc_graczy, self.wysokosc_graczy)
        pygame.draw.rect(self.screen, BLACK, self.gracz1.gr1)
        self.gracz1.hitbox_lewy = pygame.Rect(self.gracz1.x, self.gracz1.y, 1, self.wysokosc_graczy)
        self.gracz1.hitbox_prawy = pygame.Rect(self.gracz1.x+self.szerokosc_graczy, self.gracz1.y, 1, self.wysokosc_graczy)
        self.gracz1.hitbox_gorny = pygame.Rect(self.gracz1.x, self.gracz1.y, self.szerokosc_graczy, 1)
        self.gracz1.hitbox_dolny = pygame.Rect(self.gracz1.x, self.gracz1.y+self.wysokosc_graczy, self.szerokosc_graczy, 1)
        pygame.draw.rect(self.screen, RED, self.gracz1.hitbox_lewy)
        pygame.draw.rect(self.screen, RED, self.gracz1.hitbox_prawy)
        pygame.draw.rect(self.screen, RED, self.gracz1.hitbox_gorny)
        pygame.draw.rect(self.screen, RED, self.gracz1.hitbox_dolny)

        #GRACZ 2
        self.gracz2.gr2 = pygame.Rect(self.gracz2.x, self.gracz2.y, self.szerokosc_graczy, self.wysokosc_graczy)
        pygame.draw.rect(self.screen, WHITE, self.gracz2.gr2)
        self.gracz2.hitbox_lewy = pygame.Rect(self.gracz2.x, self.gracz2.y, 1, self.wysokosc_graczy)
        self.gracz2.hitbox_prawy = pygame.Rect(self.gracz2.x+self.szerokosc_graczy, self.gracz2.y, 1, self.wysokosc_graczy)
        self.gracz2.hitbox_gorny = pygame.Rect(self.gracz2.x, self.gracz2.y, self.szerokosc_graczy, 1)
        self.gracz2.hitbox_dolny = pygame.Rect(self.gracz2.x, self.gracz2.y+self.wysokosc_graczy, self.szerokosc_graczy, 1)
        pygame.draw.rect(self.screen, RED, self.gracz2.hitbox_lewy)
        pygame.draw.rect(self.screen, RED, self.gracz2.hitbox_prawy)
        pygame.draw.rect(self.screen, RED, self.gracz2.hitbox_gorny)
        pygame.draw.rect(self.screen, RED, self.gracz2.hitbox_dolny)

        #PIŁKA
        #self.pilka.pilka = pygame.Rect(self.pilka.x_pilki, self.pilka.y_pilki, 2*self.pilka.promien_pilki, 2*self.pilka.promien_pilki)
        #pygame.draw.rect(self.screen, RED, self.pilka.pilka)
        self.pilka = pygame.Rect(self.x_pilki, self.y_pilki, 2*self.promien_pilki, 2*self.promien_pilki)
        pygame.draw.rect(self.screen, RED, self.pilka)
        #pygame.draw.circle(self.screen, GREEN, self.pozycja_pilki, self.promien_pilki)

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
        if self.odbicia > self.max_dozwolonych_odbic:
            self.foxygame = False
            self.punkty_gracz2 += 1
        if self.odbicia2 > self.max_dozwolonych_odbic:
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
                self.dx_pilki = -(self.x_siatki+(self.szerokosc_siatki/2)-(self.x_pilki+self.promien_pilki))*self.szybkosc_pilki_x/(self.szerokosc_siatki/2)
            elif self.dx_pilki > 0:
                self.dx_pilki = -(self.x_siatki+(self.szerokosc_siatki/2)-(self.x_pilki+self.promien_pilki))*self.szybkosc_pilki_x/(self.szerokosc_siatki/2)
            else:
                while self.dx_pilki == 0:
                    self.dx_pilki = randrange(-10, 10)
                    self.dx_pilki /= 10
            self.dy_pilki = self.wysokosc_odbicia_pilki_od_siatki
        #JESLI GRACZ 1 JA DOTKNIE:
        if pygame.Rect.colliderect(self.gracz1.hitbox_gorny, self.pilka) and not pygame.Rect.colliderect(self.gracz1.hitbox_dolny, self.pilka):
            gracz_a_pilka = (self.gracz1.x+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))
            if gracz_a_pilka < 0:
                self.dx_pilki = -(self.gracz1.x+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))/(self.szerokosc_graczy/2)*self.szybkosc_pilki_x
            else:
                self.dx_pilki = -(self.gracz1.x+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))/(self.szerokosc_graczy/2)*self.szybkosc_pilki_x
        #JESLI GRACZ 2 JA DOTKNIE:
        if pygame.Rect.colliderect(self.gracz2.hitbox_gorny, self.pilka) and not pygame.Rect.colliderect(self.gracz2.hitbox_dolny, self.pilka):
            gracz_a_pilka2 = (self.gracz2.x+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))
            if gracz_a_pilka2 < 0:
                self.dx_pilki = -(self.gracz2.x+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))/(self.szerokosc_graczy/2)*self.szybkosc_pilki_x
            else:
                self.dx_pilki = -(self.gracz2.x+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))/(self.szerokosc_graczy/2)*self.szybkosc_pilki_x
        #JESLI GRACZ 1 UDERZA PILKE
        if pygame.Rect.colliderect(self.gracz1.hitbox_gorny, self.pilka) and self.y_pilki<=self.gracz1.y:
            self.dy_pilki = self.wysokosc_odbicia_pilki_przez_gracza
            self.y_pilki = self.gracz1.y - self.promien_pilki*2
            self.odbicia += 1
        elif pygame.Rect.colliderect(self.gracz1.hitbox_dolny, self.pilka) and self.y_pilki>self.gracz1.y:
            self.dy_pilki = -self.wysokosc_odbicia_pilki_przez_gracza
            self.y_pilki = self.gracz1.y + self.promien_pilki*2
        #JESLI GRACZ 2 UDERZA PILKE
        if pygame.Rect.colliderect(self.gracz2.hitbox_gorny, self.pilka) and self.y_pilki<=self.gracz2.y:
            self.dy_pilki = self.wysokosc_odbicia_pilki_przez_gracza
            self.y_pilki = self.gracz2.y - self.promien_pilki*2
            self.odbicia2 += 1
        elif pygame.Rect.colliderect(self.gracz2.hitbox_dolny, self.pilka) and self.y_pilki>self.gracz2.y:
            self.dy_pilki = -self.wysokosc_odbicia_pilki_przez_gracza
            self.y_pilki = self.gracz2.y + self.promien_pilki*2

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
menu()
while gameplay:
    punkty_graczy = Game(punkty_graczy).zwroc_wynik()
    print("Obecny wynik: {}/{}".format(punkty_graczy[0], punkty_graczy[1]))
    if punkty_graczy[0] >= max_liczba_punktow:
        print("Gracz 1 WYGRAŁ!")
        punkty_graczy = [0, 0]
        menu()
        #gameplay = False
    elif punkty_graczy[1] >= max_liczba_punktow:
        print("Gracz 2 WYGRAŁ!")
        punkty_graczy = [0, 0]
        menu()
        #gameplay = False

