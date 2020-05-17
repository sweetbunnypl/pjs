import pygame
from random import randint
from random import randrange

from settings.settings import settings
from static_objects.static import static
from players.gracz1 import gracz1
from players.gracz2 import gracz2
#from players.bot import bot

class pilka(object):
    #pilka
    def __init__(self):
        pass
#        #ELEMENTY POTRZEBNE:
#        #settings
#        self.foxygame = settings().foxygame
#        self.WIDTH = settings().WIDTH
#        self.HEIGHT = settings().HEIGHT
#        self.g = settings().g
#        self.dt = settings().dt
#        self.szerokosc_graczy = settings().szerokosc_graczy
#        self.wysokosc_graczy = settings().wysokosc_graczy
#        self.wysokosc_skoku = settings().wysokosc_skoku
#        self.szybkosc_poruszania = settings().szybkosc_poruszania
#        self.max_dozwolonych_odbic = settings().max_dozwolonych_odbic
#        self.max_liczba_punktow = settings().max_liczba_punktow
#        self.wysokosc_odbicia_pilki_przez_gracza = settings().wysokosc_odbicia_pilki_przez_gracza
#        self.wysokosc_odbicia_pilki_od_siatki = settings().wysokosc_odbicia_pilki_od_siatki
#        self.szybkosc_pilki_x = settings().szybkosc_pilki_x
#        #static
#        self.szerokosc_siatki = static().szerokosc_siatki
#        self.wysokosc_siatki = static().wysokosc_siatki
#        self.x_siatki = static().x_siatki
#        self.y_siatki = static().y_siatki
#        self.siatka = static().siatka
#        self.hitbox_siatka_lewy = static().hitbox_siatka_lewy
#        self.hitbox_siatka_prawy = static().hitbox_siatka_prawy
#        self.hitbox_siatka_gorny = static().hitbox_siatka_gorny
#        self.hitbox_siatka_dolny = static().hitbox_siatka_dolny
#        self.podloga = static().podloga
#        self.lewa_ramka = static().lewa_ramka
#        self.prawa_ramka = static().prawa_ramka
#        self.sufit = static().sufit
#        self.srodek = static().srodek
#        #PIŁKA:
#        self.pilka = pygame.Rect(0, 0, 0, 0)
#        self.promien_pilki = 25
#        self.x_pilki = 0.5*self.WIDTH-self.promien_pilki
#        self.y_pilki = 0.2*self.HEIGHT
#        self.dx_pilki = 0
#        #GRACZE:
#        self.gracz1 = gracz1()
#        self.gracz2 = gracz2()
#        #PUNKTY:
#        self.odbicia = 0
#        self.odbicia2 = 0
#        self.punkty_gracz2 = 0
#        self.punkty_gracz1 = 0
#
#        #LOSOWANIE POCZATKOWYCH WARTOSCI: 
#        while self.dx_pilki == 0:
#            self.dx_pilki = randrange(-10, 10)
#        self.dx_pilki /= 10
#        self.dy_pilki = randrange(-20, -10)
#
#    def ruch(self):
#        #JESLI PRZEJDZIE NA DRUGA STRONE
#        if pygame.Rect.colliderect(self.srodek, self.pilka):
#            self.odbicia = 0
#            self.odbicia2 = 0
#        #JESLI ODBIJE SIE OD PODLOGI
#        if pygame.Rect.colliderect(self.podloga, self.pilka) and self.x_pilki+self.promien_pilki<self.x_siatki+(self.szerokosc_siatki/2):
#            self.dy_pilki = -60
#            self.foxygame = False
#            self.punkty_gracz2 += 1
#        if pygame.Rect.colliderect(self.podloga, self.pilka) and self.x_pilki+self.promien_pilki>self.x_siatki+(self.szerokosc_siatki/2):
#            self.dy_pilki = -60
#            self.foxygame = False
#            self.punkty_gracz1 += 1
#        #JESLI GRACZ ODBIJE JA PONAD 3 RAZY
#        if self.odbicia >= 4:
#            self.foxygame = False
#            self.punkty_gracz2 += 1
#        if self.odbicia2 >= 4:
#            self.foxygame = False
#            self.punkty_gracz1 += 1
#        #JESLI ODBIJE SIE OD SUFITU
#        if pygame.Rect.colliderect(self.sufit, self.pilka):
#            self.dy_pilki *= -1
#        #JESLI DOTKNIE LEWEJ LUB PRAWEJ STRONY SIATKI/PLANSZY
#        if pygame.Rect.colliderect(self.lewa_ramka, self.pilka) or pygame.Rect.colliderect(self.prawa_ramka, self.pilka) or pygame.Rect.colliderect(self.hitbox_siatka_prawy, self.pilka) or pygame.Rect.colliderect(self.hitbox_siatka_lewy, self.pilka):
#            self.dx_pilki *= -1
#        #JESLI DOTKNIE GORY SIATKI
#        if pygame.Rect.colliderect(self.hitbox_siatka_gorny, self.pilka):
#            if self.dx_pilki < 0:
#                self.dx_pilki = -(self.x_siatki+(self.szerokosc_siatki/2)-(self.x_pilki+self.promien_pilki))/(self.szerokosc_siatki/2)
#            elif self.dx_pilki > 0:
#                self.dx_pilki = -(self.x_siatki+(self.szerokosc_siatki/2)-(self.x_pilki+self.promien_pilki))/(self.szerokosc_siatki/2)
#            else:
#                while self.dx_pilki == 0:
#                    self.dx_pilki = randrange(-10, 10)
#                    self.dx_pilki /= 10
#            self.dy_pilki = -40
#        #JESLI GRACZ 1 JA DOTKNIE:
#        if pygame.Rect.colliderect(self.gracz1.hitbox_gorny, self.pilka) and not pygame.Rect.colliderect(self.gracz1.hitbox_dolny, self.pilka):
#            gracz_a_pilka = (self.gracz1.x+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))
#            if gracz_a_pilka < 0:
#                self.dx_pilki = -gracz_a_pilka/(self.szerokosc_graczy/2)*5
#            else:
#                self.dx_pilki = -gracz_a_pilka/(self.szerokosc_graczy/2)*5
#        #JESLI GRACZ 2 JA DOTKNIE:
#        if pygame.Rect.colliderect(self.gracz2.hitbox_gorny, self.pilka) and not pygame.Rect.colliderect(self.gracz2.hitbox_dolny, self.pilka):
#            gracz_a_pilka2 = (self.gracz2.x+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))
#            if gracz_a_pilka2 < 0:
#                self.dx_pilki = -(self.gracz2.x+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))/(self.szerokosc_graczy/2)*5
#            else:
#                self.dx_pilki = -(self.gracz2.x+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))/(self.szerokosc_graczy/2)*5
#        #JESLI GRACZ 1 UDERZA PILKE
#        if pygame.Rect.colliderect(self.gracz1.hitbox_gorny, self.pilka) and self.y_pilki<=self.gracz1.y:
#            self.dy_pilki = -80
#            self.y_pilki = self.gracz1.y - self.promien_pilki*2
#            self.odbicia += 1
#        elif pygame.Rect.colliderect(self.gracz1.hitbox_dolny, self.pilka) and self.y_pilki>self.gracz1.y:
#            self.dy_pilki = 80
#            self.y_pilki = self.gracz1.y + self.promien_pilki*2
#        #JESLI GRACZ 2 UDERZA PILKE
#        if pygame.Rect.colliderect(self.gracz2.hitbox_gorny, self.pilka) and self.y_pilki<=self.gracz2.y:
#            self.dy_pilki = -80
#            self.y_pilki = self.gracz2.y - self.promien_pilki*2
#            self.odbicia2 += 1
#        elif pygame.Rect.colliderect(self.gracz2.hitbox_dolny, self.pilka) and self.y_pilki>self.gracz2.y:
#            self.dy_pilki = 80
#            self.y_pilki = self.gracz2.y + self.promien_pilki*2
#
#        self.dy_pilki = self.dy_pilki + self.g * self.dt
#        self.y_pilki = self.y_pilki + self.dy_pilki * self.dt
#        self.x_pilki += self.dx_pilki
#
#        #self.pozycja_pilki = (int(self.x_pilki+self.promien_pilki), int(self.y_pilki+self.promien_pilki))