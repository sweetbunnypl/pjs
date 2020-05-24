#IMPORT STANDARDOWYCH BIBLIOTEK:
import pygame, sys
from random import randint
from random import randrange
from os import system
system('clear')
#IMPORT WLASNYCH:
from players.gracz1 import gracz1
from players.gracz2 import gracz2
#from players.bot import bot
from menu.game_menu import menu
from settings.settings import settings
from static_objects.static import static
from ball.ball import pilka

#max_liczba_punktow = settings().max_liczba_punktow
#
#WIDTH = settings().WIDTH
#HEIGHT = settings().HEIGHT
#BLACK = settings().BLACK
#WHITE = settings().WHITE
#GREEN = settings().GREEN
#GRAY = settings().GRAY
#RED = settings().RED

class Game(object):

    def __init__(self, punkty_graczy):
        pygame.mixer.pre_init(22050, -16, 2, 1024)
        pygame.init()
        pygame.mixer.quit()
        pygame.mixer.init(22050, -16, 2, 1024)
        pygame.mixer.music.load('music/background_music.mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        self.uderzenie1 = pygame.mixer.Sound('music/bounce_1.wav')
        self.uderzenie2 = pygame.mixer.Sound('music/bounce_2.wav')
        self.uderzenie3 = pygame.mixer.Sound('music/bounce_3.wav')
        font = pygame.font.Font('fonts/ostrich-regular.ttf', 32)
        font0 = pygame.font.Font('fonts/ostrich-heavy.otf', 78)
        font1 = pygame.font.Font('fonts/ostrich-heavy.otf', 60)
        #USTAWIENIA
        self.g = settings().g
        self.dt = settings().dt
        self.max_fps = settings().max_fps
        self.max_dozwolonych_odbic = settings().max_dozwolonych_odbic
        self.max_liczba_punktow = settings().max_liczba_punktow
        self.wysokosc_odbicia_pilki_przez_gracza = settings().wysokosc_odbicia_pilki_przez_gracza
        self.wysokosc_odbicia_pilki_od_siatki = settings().wysokosc_odbicia_pilki_od_siatki
        self.szybkosc_pilki_x = settings().szybkosc_pilki_x
        self.WIDTH = settings().WIDTH
        self.HEIGHT = settings().HEIGHT
        self.BLACK = settings().BLACK
        self.WHITE = settings().WHITE
        self.GREEN = settings().GREEN
        self.GRAY = settings().GRAY
        self.RED = settings().RED
        self.ORANGE = settings().ORANGE
        self.mnoznik_obiektow = settings().mnoznik_obiektow

        #SCREEN
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption('The Foxyball Game')
        self.background = pygame.transform.scale(pygame.image.load('textures/background.png'), (self.WIDTH, self.HEIGHT))

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
        self.promien_pilki = settings().promien_pilki
        self.x_pilki = 0.5*self.WIDTH-self.promien_pilki
        self.y_pilki = 0.2*self.HEIGHT
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
            #WYŚWIETLANIE OBIEKTÓW:
            self.screen.blit(self.background, (0, 0))
            self.rysuj()
            #WYŚWIETLANIE PUNKTÓW:
            text1 = font1.render("%d : %d" % (self.punkty_gracz1, self.punkty_gracz2), True, self.BLACK)#, self.GRAY)
            textRect1 = text1.get_rect()
            textRect1.center = (self.WIDTH/2, 75*self.mnoznik_obiektow)
            self.screen.blit(text1, textRect1)
            if self.punkty_gracz2 >= self.max_liczba_punktow:
                text3 = font0.render("GRACZ 2 WYGRAL!", True, self.BLACK)
                textRect3 = text3.get_rect()
                textRect3.center = (self.WIDTH/2, 200*self.mnoznik_obiektow)
                self.screen.blit(text3, textRect3)
            elif self.punkty_gracz1 >= self.max_liczba_punktow:
                text3 = font0.render("GRACZ 2 WYGRAL!", True, self.BLACK)
                textRect3 = text3.get_rect()
                textRect3.center = (self.WIDTH/2, 200*self.mnoznik_obiektow)
                self.screen.blit(text3, textRect3)
            self.clock.tick(60)
            pygame.display.flip()
        self.zwroc_wynik()

    def rysuj(self):
        #PODŁOGA:
        pygame.draw.rect(self.screen, self.RED, self.podloga)
        #LEWA RAMKA:
        pygame.draw.rect(self.screen, self.RED, self.lewa_ramka)
        #PRAWA RAMKA:
        pygame.draw.rect(self.screen, self.RED, self.prawa_ramka)
        #SUFIT:
        pygame.draw.rect(self.screen, self.RED, self.sufit)
        #ŚRODEK:
        pygame.draw.rect(self.screen, self.RED, self.srodek)
        #SIATKA:
        pygame.draw.rect(self.screen, self.GRAY, self.siatka)
        #HITBOXY SIATKI:
        pygame.draw.rect(self.screen, self.RED, self.hitbox_siatka_lewy)
        pygame.draw.rect(self.screen, self.RED, self.hitbox_siatka_prawy)
        pygame.draw.rect(self.screen, self.RED, self.hitbox_siatka_gorny)
        pygame.draw.rect(self.screen, self.RED, self.hitbox_siatka_dolny)

        #GRACZ 1
        self.gracz1.gr1 = pygame.Rect(self.gracz1.x, self.gracz1.y, self.szerokosc_graczy, self.wysokosc_graczy)
        pygame.draw.rect(self.screen, self.BLACK, self.gracz1.gr1)
        self.gracz1.hitbox_lewy = pygame.Rect(self.gracz1.x, self.gracz1.y, 1, self.wysokosc_graczy)
        self.gracz1.hitbox_prawy = pygame.Rect(self.gracz1.x+self.szerokosc_graczy, self.gracz1.y, 1, self.wysokosc_graczy)
        self.gracz1.hitbox_gorny = pygame.Rect(self.gracz1.x, self.gracz1.y, self.szerokosc_graczy, 1)
        self.gracz1.hitbox_dolny = pygame.Rect(self.gracz1.x, self.gracz1.y+self.wysokosc_graczy, self.szerokosc_graczy, 1)
        pygame.draw.rect(self.screen, self.RED, self.gracz1.hitbox_lewy)
        pygame.draw.rect(self.screen, self.RED, self.gracz1.hitbox_prawy)
        pygame.draw.rect(self.screen, self.RED, self.gracz1.hitbox_gorny)
        pygame.draw.rect(self.screen, self.RED, self.gracz1.hitbox_dolny)

        #GRACZ 2
        self.gracz2.gr2 = pygame.Rect(self.gracz2.x, self.gracz2.y, self.szerokosc_graczy, self.wysokosc_graczy)
        pygame.draw.rect(self.screen, self.WHITE, self.gracz2.gr2)
        self.gracz2.hitbox_lewy = pygame.Rect(self.gracz2.x, self.gracz2.y, 1, self.wysokosc_graczy)
        self.gracz2.hitbox_prawy = pygame.Rect(self.gracz2.x+self.szerokosc_graczy, self.gracz2.y, 1, self.wysokosc_graczy)
        self.gracz2.hitbox_gorny = pygame.Rect(self.gracz2.x, self.gracz2.y, self.szerokosc_graczy, 1)
        self.gracz2.hitbox_dolny = pygame.Rect(self.gracz2.x, self.gracz2.y+self.wysokosc_graczy, self.szerokosc_graczy, 1)
        pygame.draw.rect(self.screen, self.RED, self.gracz2.hitbox_lewy)
        pygame.draw.rect(self.screen, self.RED, self.gracz2.hitbox_prawy)
        pygame.draw.rect(self.screen, self.RED, self.gracz2.hitbox_gorny)
        pygame.draw.rect(self.screen, self.RED, self.gracz2.hitbox_dolny)

        #PIŁKA
        #self.pilka.pilka = pygame.Rect(self.pilka.x_pilki, self.pilka.y_pilki, 2*self.pilka.promien_pilki, 2*self.pilka.promien_pilki)
        #pygame.draw.rect(self.screen, self.RED, self.pilka.pilka)
        self.pilka = pygame.Rect(self.x_pilki, self.y_pilki, 2*self.promien_pilki, 2*self.promien_pilki)
        pygame.draw.rect(self.screen, self.RED, self.pilka)
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
            self.wybierz_dzwiek()
        if pygame.Rect.colliderect(self.podloga, self.pilka) and self.x_pilki+self.promien_pilki>self.x_siatki+(self.szerokosc_siatki/2):
            self.dy_pilki = -60
            self.foxygame = False
            self.punkty_gracz1 += 1
            self.wybierz_dzwiek()
        #JESLI GRACZ ODBIJE JA PONAD MAX RAZY
        if self.odbicia > self.max_dozwolonych_odbic:
            self.foxygame = False
            self.punkty_gracz2 += 1

        if self.odbicia2 > self.max_dozwolonych_odbic:
            self.foxygame = False
            self.punkty_gracz1 += 1
        #JESLI ODBIJE SIE OD SUFITU
        if pygame.Rect.colliderect(self.sufit, self.pilka):
            self.dy_pilki *= -1
            self.wybierz_dzwiek()
        #JESLI DOTKNIE LEWEJ LUB PRAWEJ STRONY SIATKI/PLANSZY
        if pygame.Rect.colliderect(self.lewa_ramka, self.pilka) or pygame.Rect.colliderect(self.prawa_ramka, self.pilka) or pygame.Rect.colliderect(self.hitbox_siatka_prawy, self.pilka) or pygame.Rect.colliderect(self.hitbox_siatka_lewy, self.pilka):
            self.dx_pilki *= -1
            self.wybierz_dzwiek()
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
            self.wybierz_dzwiek()
        #JESLI GRACZ 1 JA DOTKNIE:
        if pygame.Rect.colliderect(self.gracz1.hitbox_gorny, self.pilka) or pygame.Rect.colliderect(self.gracz1.hitbox_dolny, self.pilka):
            gracz_a_pilka = (self.gracz1.x+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))
            if gracz_a_pilka < 0:
                self.dx_pilki = -(self.gracz1.x+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))*self.szybkosc_pilki_x/(self.szerokosc_graczy/2)
            else:
                self.dx_pilki = -(self.gracz1.x+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))*self.szybkosc_pilki_x/(self.szerokosc_graczy/2)
        if pygame.Rect.colliderect(self.gracz1.hitbox_lewy, self.pilka) and not (pygame.Rect.colliderect(self.gracz1.hitbox_gorny, self.pilka) or pygame.Rect.colliderect(self.gracz1.hitbox_dolny, self.pilka)):
            self.dx_pilki *= -1
            self.x_pilki = self.gracz1.x-self.promien_pilki*2
        if pygame.Rect.colliderect(self.gracz1.hitbox_prawy, self.pilka) and not (pygame.Rect.colliderect(self.gracz1.hitbox_gorny, self.pilka) or pygame.Rect.colliderect(self.gracz1.hitbox_dolny, self.pilka)):
            self.dx_pilki *= -1
            self.x_pilki = self.gracz1.x+self.szerokosc_graczy
        #JESLI GRACZ 2 JA DOTKNIE:
        if pygame.Rect.colliderect(self.gracz2.hitbox_gorny, self.pilka) or pygame.Rect.colliderect(self.gracz2.hitbox_dolny, self.pilka):
            gracz_a_pilka2 = (self.gracz2.x+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))
            if gracz_a_pilka2 < 0:
                self.dx_pilki = -(self.gracz2.x+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))*self.szybkosc_pilki_x/(self.szerokosc_graczy/2)
            else:
                self.dx_pilki = -(self.gracz2.x+(self.szerokosc_graczy/2)-(self.x_pilki+self.promien_pilki))*self.szybkosc_pilki_x/(self.szerokosc_graczy/2)
        if pygame.Rect.colliderect(self.gracz2.hitbox_lewy, self.pilka) and not (pygame.Rect.colliderect(self.gracz2.hitbox_gorny, self.pilka) or pygame.Rect.colliderect(self.gracz2.hitbox_dolny, self.pilka)):
            self.dx_pilki *= -1
            self.x_pilki = self.gracz2.x-self.promien_pilki*2
        if pygame.Rect.colliderect(self.gracz2.hitbox_prawy, self.pilka) and not (pygame.Rect.colliderect(self.gracz2.hitbox_gorny, self.pilka) or pygame.Rect.colliderect(self.gracz2.hitbox_dolny, self.pilka)):
            self.dx_pilki *= -1
            self.x_pilki = self.gracz2.x+self.szerokosc_graczy
        #JESLI GRACZ 1 UDERZA PILKE
        if pygame.Rect.colliderect(self.gracz1.hitbox_gorny, self.pilka) and self.y_pilki<=self.gracz1.y:
            self.dy_pilki = self.wysokosc_odbicia_pilki_przez_gracza
            #self.y_pilki = self.gracz1.y - self.promien_pilki*2
            self.odbicia += 1
            self.wybierz_dzwiek()
        elif pygame.Rect.colliderect(self.gracz1.hitbox_dolny, self.pilka) and self.y_pilki>self.gracz1.y:
            self.dy_pilki = -self.wysokosc_odbicia_pilki_przez_gracza
            self.y_pilki = self.gracz1.y + self.wysokosc_graczy
            self.wybierz_dzwiek()
        #JESLI GRACZ 2 UDERZA PILKE
        if pygame.Rect.colliderect(self.gracz2.hitbox_gorny, self.pilka) and self.y_pilki<=self.gracz2.y:
            self.dy_pilki = self.wysokosc_odbicia_pilki_przez_gracza
            #self.y_pilki = self.gracz2.y - self.promien_pilki*2
            self.odbicia2 += 1
            self.wybierz_dzwiek()
        elif pygame.Rect.colliderect(self.gracz2.hitbox_dolny, self.pilka) and self.y_pilki>self.gracz2.y:
            self.dy_pilki = -self.wysokosc_odbicia_pilki_przez_gracza
            self.y_pilki = self.gracz2.y + self.wysokosc_graczy
            self.wybierz_dzwiek()

        self.dy_pilki = self.dy_pilki + self.g * self.dt
        self.y_pilki = self.y_pilki + self.dy_pilki * self.dt
        self.x_pilki += self.dx_pilki

        #self.pozycja_pilki = (int(self.x_pilki+self.promien_pilki), int(self.y_pilki+self.promien_pilki))

    def wybierz_dzwiek(self):
        wybor_dzwieku = randrange(0, 100)
        if wybor_dzwieku >= 33:
            self.uderzenie1.play()
        elif wybor_dzwieku < 33 and wybor_dzwieku >= 67:
            self.uderzenie2.play()
        else:
            self.uderzenie3.play()
    
    def zwroc_wynik(self):
        return [self.punkty_gracz1, self.punkty_gracz2]

def foxyball_game():
    #play_music()
    gameplay = True
    punkty_gracz1 = 0
    punkty_gracz2 = 0
    punkty_graczy = [punkty_gracz1, punkty_gracz2]
    while gameplay:
        if punkty_graczy == [0, 0]:
            menu()
        max_liczba_punktow = settings().max_liczba_punktow
        punkty_graczy = Game(punkty_graczy).zwroc_wynik()
        print("Obecny wynik: {}/{}".format(punkty_graczy[0], punkty_graczy[1]))
        if punkty_graczy[0] >= max_liczba_punktow:
            print("Gracz 1 WYGRAŁ!")
            punkty_graczy = [0, 0]
            pygame.mixer.music.fadeout(3500)
            pygame.time.wait(4000)
        elif punkty_graczy[1] >= max_liczba_punktow:
            print("Gracz 2 WYGRAŁ!")
            punkty_graczy = [0, 0]
            pygame.mixer.music.fadeout(3500)
            pygame.time.wait(4000)

foxyball_game()
