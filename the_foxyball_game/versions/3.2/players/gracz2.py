import pygame
from settings.settings import settings
from static_objects.static import static

class gracz2(object):
    #gracz 2
    def __init__(self):
        #ELEMENTY POTRZEBNE:
        #settings
        self.WIDTH = settings().WIDTH
        self.HEIGHT = settings().HEIGHT
        self.g = settings().g
        self.dt = settings().dt
        self.wysokosc_skoku = settings().wysokosc_skoku
        self.szybkosc_poruszania = settings().szybkosc_poruszania
        #static
        self.hitbox_siatka_prawy = static().hitbox_siatka_prawy
        self.prawa_ramka = static().prawa_ramka
        self.podloga = static().podloga
        #INICJALIZACJA ELEMENTOW GRACZA:
        self.gr2 = pygame.Rect(0, 0, 0, 0)
        self.hitbox_lewy = pygame.Rect(0, 0, 0, 0)
        self.hitbox_prawy = pygame.Rect(0, 0, 0, 0)
        self.hitbox_gorny = pygame.Rect(0, 0, 0, 0)
        self.hitbox_dolny = pygame.Rect(0, 0, 0, 0)
        #POCZATKOWE WARTOSCI:
        self.x = 0.8*self.WIDTH
        self.y = 0.8*self.HEIGHT
        self.dx = 0
        self.dy = 0
        self.lot = 0
        self.keys = [0,0,0,0] #[I,K,J,L]

    def odczyt_klawiszy(self):
        klawiatura = pygame.key.get_pressed()
        if klawiatura[pygame.K_l] and not pygame.Rect.colliderect(self.prawa_ramka, self.gr2):
            self.keys[3] = 1
        else:
            self.keys[3] = 0
            
        if klawiatura[pygame.K_j] and not pygame.Rect.colliderect(self.hitbox_siatka_prawy, self.gr2):
            self.keys[2] = 1
        else:
            self.keys[2] = 0
        
        if klawiatura[pygame.K_i] and not self.lot:
            self.keys[0] = 1
            self.lot = 1
            self.dy = self.wysokosc_skoku
        else:
            self.keys[0] = 0

    def ruch(self):
        self.dx = 0
        if self.keys[2]:
            self.dx -= self.szybkosc_poruszania
        if self.keys[3]:
            self.dx += self.szybkosc_poruszania

        if self.lot:
            self.dy = self.dy + self.g * self.dt
            self.y = self.y + self.dy * self.dt

        if self.lot and pygame.Rect.colliderect(self.podloga, self.gr2):
            self.dy = 0
            self.lot = 0
            self.y = 0.8*self.HEIGHT

        self.x += self.dx * self.dt