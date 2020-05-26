import pygame
from settings.settings import settings
from static_objects.static import static

class gracz1(object):#(pygame.sprite.Sprite):
    #gracz 1
    def __init__(self):#, color, width, height):
        #pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load('textures/background.png')
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        #self.image = pygame.Surface([width, height])
        #self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        #self.rect = self.image.get_rect()
        self.textura_lewo = [pygame.image.load('textures/foxy/L0.png'), pygame.image.load('textures/foxy/L1.png'), pygame.image.load('textures/foxy/L2.png'), pygame.image.load('textures/foxy/L3.png'), pygame.image.load('textures/foxy/L4.png'), pygame.image.load('textures/foxy/L5.png'), pygame.image.load('textures/foxy/L6.png'), pygame.image.load('textures/foxy/L7.png'), pygame.image.load('textures/foxy/L8.png'), pygame.image.load('textures/foxy/L9.png'), pygame.image.load('textures/foxy/L10.png'), pygame.image.load('textures/foxy/L11.png'), pygame.image.load('textures/foxy/L12.png'), pygame.image.load('textures/foxy/L13.png'), pygame.image.load('textures/foxy/L14.png'), pygame.image.load('textures/foxy/L15.png'), pygame.image.load('textures/foxy/L16.png'), pygame.image.load('textures/foxy/L17.png'), pygame.image.load('textures/foxy/L18.png'), pygame.image.load('textures/foxy/L19.png'), pygame.image.load('textures/foxy/L20.png'), pygame.image.load('textures/foxy/L21.png'), pygame.image.load('textures/foxy/L22.png'), pygame.image.load('textures/foxy/L23.png')]
        self.textura_prawo = [pygame.image.load('textures/foxy/P0.png'), pygame.image.load('textures/foxy/P1.png'), pygame.image.load('textures/foxy/P2.png'), pygame.image.load('textures/foxy/P3.png'), pygame.image.load('textures/foxy/P4.png'), pygame.image.load('textures/foxy/P5.png'), pygame.image.load('textures/foxy/P6.png'), pygame.image.load('textures/foxy/P7.png'), pygame.image.load('textures/foxy/P8.png'), pygame.image.load('textures/foxy/P9.png'), pygame.image.load('textures/foxy/P10.png'), pygame.image.load('textures/foxy/P11.png'), pygame.image.load('textures/foxy/P12.png'), pygame.image.load('textures/foxy/P13.png'), pygame.image.load('textures/foxy/P14.png'), pygame.image.load('textures/foxy/P15.png'), pygame.image.load('textures/foxy/P16.png'), pygame.image.load('textures/foxy/P17.png'), pygame.image.load('textures/foxy/P18.png'), pygame.image.load('textures/foxy/P19.png'), pygame.image.load('textures/foxy/P20.png'), pygame.image.load('textures/foxy/P21.png'), pygame.image.load('textures/foxy/P22.png'), pygame.image.load('textures/foxy/P23.png')]
        self.walkcount_left = 0
        self.walkcount_right = 0
        self.picture = self.textura_prawo[0]
        #ELEMENTY POTRZEBNE:
        #settings
        self.WIDTH = settings().WIDTH
        self.HEIGHT = settings().HEIGHT
        self.g = settings().g
        self.dt = settings().dt
        self.wysokosc_skoku = settings().wysokosc_skoku
        self.szybkosc_poruszania = settings().szybkosc_poruszania
        self.szerokosc_graczy = settings().szerokosc_graczy
        self.wysokosc_graczy = settings().wysokosc_graczy
        self.mnoznik_obiektow = settings().mnoznik_obiektow
        #static
        self.hitbox_siatka_lewy = static().hitbox_siatka_lewy
        self.lewa_ramka = static().lewa_ramka
        self.hitbox_siatka_prawy = static().hitbox_siatka_prawy
        self.prawa_ramka = static().prawa_ramka
        self.podloga = static().podloga
        #INICJALIZACJA ELEMENTOW GRACZA:
        self.gr1 = pygame.Rect(0, 0, 0, 0)
        self.hitbox_lewy = pygame.Rect(0, 0, 0, 0)
        self.hitbox_prawy = pygame.Rect(0, 0, 0, 0)
        self.hitbox_gorny = pygame.Rect(0, 0, 0, 0)
        self.hitbox_dolny = pygame.Rect(0, 0, 0, 0)
        #POCZATKOWE WARTOSCI:
        self.x = self.WIDTH/2 - (400+self.szerokosc_graczy/2)*self.mnoznik_obiektow
        self.y = 0.8*self.HEIGHT
        self.dx = 0
        self.dy = 0
        self.lot = 0
        self.keys = [0,0,0,0] #[W,S,A,D]

        #self.picture = pygame.image.load('textures/background.png')
        #self.picture = pygame.transform.scale(self.picture, (self.szerokosc_graczy, self.wysokosc_graczy))

    def odczyt_klawiszy(self):
        klawiatura = pygame.key.get_pressed()
        if klawiatura[pygame.K_d] and not pygame.Rect.colliderect(self.hitbox_siatka_lewy, self.gr1) and not pygame.Rect.colliderect(self.prawa_ramka, self.gr1):
            self.keys[3] = 1
        else:
            self.keys[3] = 0

        if klawiatura[pygame.K_a] and not pygame.Rect.colliderect(self.lewa_ramka, self.gr1) and not pygame.Rect.colliderect(self.hitbox_siatka_prawy, self.gr1):
            self.keys[2] = 1
        else:
            self.keys[2] = 0

        if klawiatura[pygame.K_w] and not self.lot:
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
        
        if self.lot and pygame.Rect.colliderect(self.podloga, self.gr1):
            self.dy = 0
            self.lot = 0
            self.y = 0.8*self.HEIGHT

        self.x += self.dx * self.dt
    
    def rysuj(self, surface, color):
        self.lisek()
        self.gr1 = pygame.Rect(self.x, self.y, self.szerokosc_graczy, self.wysokosc_graczy)
        #pygame.draw.rect(surface, color, self.gr1)
        surface(self.picture, self.gr1)
    
    def lisek(self):
        if self.keys[3] and self.keys[2]:
            pass
        elif self.keys[3]:
            self.walkcount_right += 1
            if self.walkcount_right >= 24:
                self.walkcount_right = 0
            self.walkcount_left = 0
            self.picture = self.textura_prawo[self.walkcount_right]
        elif self.keys[2]:
            self.walkcount_left += 1
            self.walkcount_right = 0
            if self.walkcount_left >= 24:
                self.walkcount_left = 0
            self.walkcount_right = 0
            self.picture = self.textura_lewo[self.walkcount_left]
        self.picture = pygame.transform.scale(self.picture, (self.szerokosc_graczy, self.wysokosc_graczy))
