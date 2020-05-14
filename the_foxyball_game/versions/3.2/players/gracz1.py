import pygame
from settings.settings import settings
from static_objects.static import static

class gracz1(object):
    #gracz 1
    def __init__(self):
        #ELEMENTY POTRZEBNE:
        #settings
        self.WIDTH = settings().WIDTH
        self.HEIGHT = settings().HEIGHT
        self.g = settings().g
        self.dt = settings().dt
        #static
        self.hitbox_siatka_lewy = static().hitbox_siatka_lewy
        self.lewa_ramka = static().lewa_ramka
        self.podloga = static().podloga
        #INICJALIZACJA ELEMENTOW GRACZA:
        self.gr1 = pygame.Rect(0, 0, 0, 0)
        self.hitbox_lewy = pygame.Rect(0, 0, 0, 0)
        self.hitbox_prawy = pygame.Rect(0, 0, 0, 0)
        self.hitbox_gorny = pygame.Rect(0, 0, 0, 0)
        self.hitbox_dolny = pygame.Rect(0, 0, 0, 0)
        #POCZATKOWE WARTOSCI:
        self.x = 0.2*self.WIDTH
        self.y = 0.8*self.HEIGHT
        self.dx = 0
        self.dy = 0
        self.lot = 0
        self.keys = [0,0,0,0] #[W,S,A,D]

    def odczyt_klawiszy(self):
        klawiatura = pygame.key.get_pressed()
        if klawiatura[pygame.K_d] and not pygame.Rect.colliderect(self.hitbox_siatka_lewy, self.gr1):
            self.keys[3] = 1
        else:
            self.keys[3] = 0

        if klawiatura[pygame.K_a] and not pygame.Rect.colliderect(self.lewa_ramka, self.gr1):
            self.keys[2] = 1
        else:
            self.keys[2] = 0

        if klawiatura[pygame.K_w] and not self.lot:
            self.keys[0] = 1
            self.lot = 1
            self.dy = -60
        else:
            self.keys[0] = 0

    def ruch(self):
        self.dx = 0
        if self.keys[2]:
            self.dx -= 40
        if self.keys[3]:
            self.dx += 40

        if self.lot:
            self.dy = self.dy + self.g * self.dt
            self.y = self.y + self.dy * self.dt
        
        if self.lot and pygame.Rect.colliderect(self.podloga, self.gr1):
            self.dy = 0
            self.lot = 0
            self.y = 0.8*self.HEIGHT

        self.x += self.dx * self.dt