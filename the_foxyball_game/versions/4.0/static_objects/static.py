import pygame
from settings.settings import settings

class static(object):
    #OBIEKTY STATYCZNE:
    def __init__(self):
        #PARAMETRY Z USTAWIEN:
        self.WIDTH = settings().WIDTH
        self.HEIGHT = settings().HEIGHT
        self.BLACK = settings().BLACK
        self.WHITE = settings().WHITE
        self.GREEN = settings().GREEN
        self.GRAY = settings().GRAY
        self.RED = settings().RED
        self.szerokosc_graczy = settings().szerokosc_graczy
        self.wysokosc_graczy = settings().wysokosc_graczy

        #SIATKA
        self.szerokosc_siatki = settings().szerokosc_siatki #self.WIDTH*0.05
        self.wysokosc_siatki = settings().wysokosc_siatki #self.HEIGHT*0.45
        self.x_siatki = (self.WIDTH-self.szerokosc_siatki)/2
        self.y_siatki = (self.HEIGHT*0.8-self.wysokosc_siatki+self.wysokosc_graczy)
        self.siatka = pygame.Rect(self.x_siatki, self.y_siatki, self.szerokosc_siatki, self.wysokosc_siatki)
        self.hitbox_siatka_lewy = pygame.Rect(self.x_siatki, self.y_siatki, 1, self.wysokosc_siatki)
        self.hitbox_siatka_prawy = pygame.Rect(self.x_siatki+self.szerokosc_siatki, self.y_siatki, 1, self.wysokosc_siatki)
        self.hitbox_siatka_gorny = pygame.Rect(self.x_siatki, self.y_siatki, self.szerokosc_siatki, 1)
        self.hitbox_siatka_dolny = pygame.Rect(self.x_siatki, self.y_siatki+self.wysokosc_siatki, self.szerokosc_siatki, 1)

        #PODŁOGA
        self.podloga = pygame.Rect(0, 0.8*self.HEIGHT+self.wysokosc_graczy, self.WIDTH, 1)
        
        #LEWA RAMKA
        self.lewa_ramka = pygame.Rect(0, 0, 1, self.HEIGHT)
        
        #PRAWA RAMKA
        self.prawa_ramka = pygame.Rect(self.WIDTH-1, 0, 1, self.HEIGHT)
        
        #SUFIT
        self.sufit = pygame.Rect(0, 0, self.WIDTH, 1)
        
        #ŚRODEK
        self.srodek = pygame.Rect(self.x_siatki+(self.szerokosc_siatki/2), 0, 1, self.HEIGHT)