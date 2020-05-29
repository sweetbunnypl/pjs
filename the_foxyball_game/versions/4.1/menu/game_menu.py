import pygame, sys, os
from settings.settings import settings
from datetime import datetime

BLACK = settings().BLACK
WHITE = settings().WHITE
GREEN = settings().GREEN
GRAY = settings().GRAY
RED = settings().RED
ORANGE = settings().ORANGE
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.quit()
pygame.mixer.init()
pygame.init()
#font0 = pygame.font.Font('fonts/ostrich-regular.ttf', 78)
#font0_0 = pygame.font.Font('fonts/ostrich-heavy.otf', 78)
#font = pygame.font.Font('fonts/ostrich-regular.ttf', 42)
#font_1 = pygame.font.Font('fonts/ostrich-heavy.otf', 42)
#font1 = pygame.font.Font('fonts/ostrich-regular.ttf', 56)
#font2 = pygame.font.Font('fonts/ostrich-regular.ttf', 28)
font0 = settings().font_72
font0_0 = settings().font_72_heavy
font = settings().font_42
font_1 = settings().font_42_heavy
font1 = settings().font_56
font2 = settings().font_28

now = datetime.now()

class menu(object):

    def __init__(self):
        self.BLACK = settings().BLACK
        self.WIDTH = settings().WIDTH
        self.HEIGHT = settings().HEIGHT
        pygame.mixer.music.load('music/menu_music.mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        self.max_fps = 60.0
        self.n = 0
        self.menu_position = [0,0,0,0]
        self.mnoznik_obiektow = settings().mnoznik_obiektow
        self.dzwiek_zmiana = pygame.mixer.Sound('music/menu_change.wav')
        self.dzwiek_enter = pygame.mixer.Sound('music/menu_enter.wav')
        self.dzwiek_wroc = pygame.mixer.Sound('music/menu_quit.wav')

        #SCREEN
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('The Foxyball Game')
        self.background = pygame.transform.scale(pygame.image.load('textures/background.png'), (self.WIDTH, self.HEIGHT))
        day_time = int(now.strftime("%H"))
        if day_time >= 4 and day_time < 16:
            self.background = pygame.transform.scale(pygame.image.load('textures/background.png'), (self.WIDTH, self.HEIGHT))
        elif day_time >=16 or day_time < 4:
            self.background = pygame.transform.scale(pygame.image.load('textures/background2.png'), (self.WIDTH, self.HEIGHT))

        self.txt7 = 0
        #PĘTLA
        self.menu_time = True
        while self.menu_time:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.dzwiek_wroc.play()
                    pygame.time.wait(500)
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.dzwiek_wroc.play()
                    pygame.time.wait(500)
                    pygame.quit()
                    sys.exit()

                self.odczyt_klawiszy()
            self.screen.blit(self.background, (0, 0))
            self.wyswietlanie_menu()
            pygame.display.flip()
            

    def wyswietlanie_menu(self):
#MAIN MENU
        txt1 = 0
        txt2 = 0
        txt3 = 0
        txt4 = 0
        txt5 = 0
        txt6 = 0
        #txt7 = 0

        if self.menu_position[0] == 0 and self.n == 0:
            text = font1.render("-  GRAJ  -", True, self.BLACK)
            txt1 = 1
        elif self.menu_position[0] != 0 and self.n == 0:
            text = font.render("GRAJ", True, self.BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.n == 0:
            text2 = font1.render("-  USTAWIENIA  -", True, self.BLACK)
            txt2 = 1
        elif self.menu_position[0] != 1 and self.n == 0:
            text2 = font.render("USTAWIENIA", True, self.BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 2 and self.n == 0:
            text3 = font1.render("-  STEROWANIE  -", True, self.BLACK)
            txt3 = 1
        elif self.menu_position[0] != 2 and self.n == 0:
            text3 = font.render("STEROWANIE", True, self.BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 3 and self.n == 0:
            text4 = font1.render("-  AUTOR  -", True, self.BLACK)
            txt4 = 1
        elif self.menu_position[0] != 3 and self.n == 0:
            text4 = font.render("AUTOR", True, self.BLACK)
            txt4 = 1
#WYSWIETLANIE POZYCJI MENU
        #text7 = font.render("numeracja menu: (%d, %d, %d, %d) n: %d" % (self.menu_position[0], self.menu_position[1], self.menu_position[2], self.menu_position[3], self.n), True, self.BLACK)
        #txt7 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #USTAWIENIA
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.n == 1:
            text = font1.render("-  ROZMIAR I PREDKOSC GRACZY  -", True, self.BLACK)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] != 0 and self.n == 1:
            text = font.render("ROZMIAR I PREDKOSC GRACZY", True, self.BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.n == 1:
            text2 = font1.render("-  WIELKOSC OKNA  -", True, self.BLACK)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] != 1 and self.n == 1:
            text2 = font.render("WIELKOSC OKNA", True, self.BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.n == 1:
            text3 = font1.render("-  FIZYKA  -", True, self.BLACK)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] != 2 and self.n == 1:
            text3 = font.render("FIZYKA", True, self.BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.n == 1:
            text4 = font1.render("-  PUNKTACJA  -", True, self.BLACK)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] != 3 and self.n == 1:
            text4 = font.render("PUNKTACJA", True, self.BLACK)
            txt4 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.n == 1:
            text5 = font1.render("-  PILKA  -", True, self.BLACK)
            txt5 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] != 4 and self.n == 1:
            text5 = font.render("PILKA", True, self.BLACK)
            txt5 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.n == 1:
            text6 = font1.render("-  SIATKA  -", True, self.BLACK)
            txt6 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] != 5 and self.n == 1:
            text6 = font.render("SIATKA", True, self.BLACK)
            txt6 = 1
#------------------------------------------------------------------------------------------------------------------------------------#                
        #STEROWANIE
        if self.menu_position[0] == 2 and self.n == 1:
            sterowanie_txt1 = 'GRACZ 1: "W"-skok  "A"-krok w lewo  "D"-krok w prawo'
            text2 = font_1.render(sterowanie_txt1, True, self.BLACK)
            sterowanie_txt2 = 'GRACZ 2: "I"-skok  "J"-krok w lewo  "L"-krok w prawo'
            text3 = font_1.render(sterowanie_txt2, True, self.BLACK)
            sterowanie_txt3 = "Klawisz 'Esc' powoduje wyjscie z gry"
            text4 = font_1.render(sterowanie_txt3, True, self.BLACK)
            txt2 = 1
            txt3 = 1
            txt4 = 1
#------------------------------------------------------------------------------------------------------------------------------------#                
        #AUTOR
        if self.menu_position[0] == 3 and self.n == 1:
            text2 = font1.render("Karol Bolanowski, ISSP rok 1", True, self.BLACK)
            txt2 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
#MENU ---> USTAWIENIA
        #ROZMIAR I PRĘDKOSC GRACZY
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.n == 2:
            text = font1.render("-  SZEROKOSC I WYSOKOSC GRACZY  -", True, self.BLACK)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] != 0 and self.n == 2:
            text = font.render("SZEROKOSC I WYSOKOSC GRACZY", True, self.BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.n == 2:
            text2 = font1.render("-  PREDKOSC SKOKU  -", True, self.BLACK)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] != 1 and self.n == 2:
            text2 = font.render("PREDKOSC SKOKU", True, self.BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.n == 2:
            text3 = font1.render("-  PREDKOSC PORUSZANIA SIE  -", True, self.BLACK)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] != 2 and self.n == 2:
            text3 = font.render("PREDKOSC PORUSZANIA SIE", True, self.BLACK)
            txt3 = 1
#------------------------------------------------------------------------------------------------------------------------------------#                
        #WIELKOSC OKNA:
        if self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.menu_position[2] == 0 and self.n == 2:
            text = font1.render("-  1280x720  -", True, self.BLACK)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.menu_position[2] != 0 and self.n == 2:
            text = font.render("1280x720", True, self.BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.menu_position[2] == 1 and self.n == 2:
            text2 = font1.render("-  1600x900  -", True, self.BLACK)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.menu_position[2] != 1 and self.n == 2:
            text2 = font.render("1600x900", True, self.BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.menu_position[2] == 2 and self.n == 2:
            text3 = font1.render("-  1920x1080  -", True, self.BLACK)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.menu_position[2] != 2 and self.n == 2:
            text3 = font.render("1920x1080", True, self.BLACK)
            txt3 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #FIZYKA:
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.n == 2:
            text = font1.render("-  STALA GRAWITACJI  -", True, self.BLACK)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] != 0 and self.n == 2:
            text = font.render("STALA GRAWITACJI", True, self.BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.n == 2:
            text2 = font1.render("-  SZYBKOSC CZASU  -", True, self.BLACK)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] != 1 and self.n == 2:
            text2 = font.render("SZYBKOSC CZASU", True, self.BLACK)
            txt2 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #PUNKTACJA:
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.n == 2:
            text = font1.render("-  MAX DOZWOLONYCH ODBIC  -", True, self.BLACK)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] != 0 and self.n == 2:
            text = font.render("MAX DOZWOLONYCH ODBIC", True, self.BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.n == 2:
            text2 = font1.render("-  ILOSC RUND  -", True, self.BLACK)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] != 1 and self.n == 2:
            text2 = font.render("ILOSC RUND", True, self.BLACK)
            txt2 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #PIŁKA:
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.n == 2:
            text = font1.render("-  PREDKOSC Y ODBICIA PILKI PRZEZ GRACZA  -", True, self.BLACK)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] != 0 and self.n == 2:
            text = font.render("PREDKOSC Y ODBICIA PILKI PRZEZ GRACZA", True, self.BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.n == 2:
            text2 = font1.render("-  PREDKOSC Y ODBICIA PILKI OD SIATKI  -", True, self.BLACK)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] != 1 and self.n == 2:
            text2 = font.render("PREDKOSC Y ODBICIA PILKI OD SIATKI", True, self.BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.n == 2:
            text3 = font1.render("-  PREDKOSC X PILKI  -", True, self.BLACK)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] != 2 and self.n == 2:
            text3 = font.render("PREDKOSC X PILKI", True, self.BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.n == 2:
            text4 = font1.render("-  PROMIEN PILKI  -", True, self.BLACK)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] != 3 and self.n == 2:
            text4 = font.render("PROMIEN PILKI", True, self.BLACK)
            txt4 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #SIATKA:
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.n == 2:
            text = font1.render("-  WYSOKOSC SIATKI  -", True, self.BLACK)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] != 0 and self.n == 2:
            text = font.render("WYSOKOSC SIATKI", True, self.BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.n == 2:
            text2 = font1.render("-  SZEROKOSC SIATKI  -", True, self.BLACK)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] != 1 and self.n == 2:
            text2 = font.render("SZEROKOSC SIATKI", True, self.BLACK)
            txt2 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
#MENU ---> USTAWIENIA ---> ROZMIAR I PREDKOSC GRACZY
        #SZEROKOSC I WYSOKOSC GRACZY
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] == 0 and self.n == 3:
            text = font1.render("-  200x100  -", True, self.BLACK)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("200x100", True, self.BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font1.render("-  100x50  -", True, self.BLACK)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("100x50", True, self.BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font1.render("-  170x85  -", True, self.BLACK)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("170x85", True, self.BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] == 3 and self.n == 3:
            text4 = font1.render("-  230x115  -", True, self.BLACK)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] != 3 and self.n == 3:
            text4 = font.render("230x115", True, self.BLACK)
            txt4 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #PREDKOSC SKOKU GRACZA
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.menu_position[3] == 0 and self.n == 3:
            text = font1.render("-  60  -", True, self.BLACK)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("60", True, self.BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font1.render("-  40  -", True, self.BLACK)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("40", True, self.BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font1.render("-  80  -", True, self.BLACK)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("80", True, self.BLACK)
            txt3 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #PREDKOSC PORUSZANIA SIE GRACZA
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.menu_position[3] == 0 and self.n == 3:
            text = font1.render("-  40  -", True, self.BLACK)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("40", True, self.BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font1.render("-  60  -", True, self.BLACK)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("60", True, self.BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font1.render("-  80  -", True, self.BLACK)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("80", True, self.BLACK)
            txt3 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
#MENU ---> USTAWIENIA ---> FIZYKA
        #STALA GRAWITACJI
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.menu_position[3] == 0 and self.n == 3:
            text = font1.render("-  9.81  -", True, self.BLACK)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("9.81", True, self.BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font1.render("-  13.81  -", True, self.BLACK)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("13.81", True, self.BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font1.render("-  5.81  -", True, self.BLACK)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("5.81", True, self.BLACK)
            txt3 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #SZYBKOSC CZASU
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] == 0 and self.n == 3:
            text = font1.render("-  0.2  -", True, self.BLACK)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("0.2", True, self.BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font1.render("-  0.1  -", True, self.BLACK)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("0.1", True, self.BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font1.render("-  0.25  -", True, self.BLACK)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("0.25", True, self.BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] == 3 and self.n == 3:
            text4 = font1.render("-  0.30  -", True, self.BLACK)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] != 3 and self.n == 3:
            text4 = font.render("0.30", True, self.BLACK)
            txt4 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
#MENU ---> USTAWIENIA ---> PUNKTACJA
        #MAX DOZWOLONYCH ODBIC
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.menu_position[3] == 0 and self.n == 3:
            text = font1.render("-  3  -", True, self.BLACK)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("3", True, self.BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font1.render("-  1  -", True, self.BLACK)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("1", True, self.BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font1.render("-  5  -", True, self.BLACK)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("5", True, self.BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.menu_position[3] == 3 and self.n == 3:
            text4 = font1.render("-  100  -", True, self.BLACK)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.menu_position[3] != 3 and self.n == 3:
            text4 = font.render("100", True, self.BLACK)
            txt4 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #ILOSC RUND
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.menu_position[3] == 0 and self.n == 3:
            text = font1.render("-  5  -", True, self.BLACK)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("5", True, self.BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font1.render("-  1  -", True, self.BLACK)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("1", True, self.BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font1.render("-  10  -", True, self.BLACK)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("10", True, self.BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.menu_position[3] == 3 and self.n == 3:
            text4 = font1.render("-  15  -", True, self.BLACK)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.menu_position[3] != 3 and self.n == 3:
            text4 = font.render("15", True, self.BLACK)
            txt4 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
#MENU ---> USTAWIENIA ---> PIŁKA
        #PREDKOSC Y ODBICIA PILKI PRZEZ GRACZA
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.menu_position[3] == 0 and self.n == 3:
            text = font1.render("-  80  -", True, self.BLACK)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("80", True, self.BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font1.render("-  40  -", True, self.BLACK)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("40", True, self.BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font1.render("-  60  -", True, self.BLACK)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("60", True, self.BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.menu_position[3] == 3 and self.n == 3:
            text4 = font1.render("-  100  -", True, self.BLACK)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.menu_position[3] != 3 and self.n == 3:
            text4 = font.render("100", True, self.BLACK)
            txt4 = 1
#------------------------------------------------------------------------------------------------------------------------------------#      
        #PREDKOSC Y ODBICIA PILKI OD SIATKI
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.menu_position[3] == 0 and self.n == 3:
            text = font1.render("-  40  -", True, self.BLACK)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("40", True, self.BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font1.render("-  20  -", True, self.BLACK)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("20", True, self.BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font1.render("-  60  -", True, self.BLACK)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("60", True, self.BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.menu_position[3] == 3 and self.n == 3:
            text4 = font1.render("-  80  -", True, self.BLACK)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.menu_position[3] != 3 and self.n == 3:
            text4 = font.render("80", True, self.BLACK)
            txt4 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #PREDKOSC X PILKI
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.menu_position[3] == 0 and self.n == 3:
            text = font1.render("-  6  -", True, self.BLACK)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("6", True, self.BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font1.render("-  2  -", True, self.BLACK)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("2", True, self.BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font1.render("-  4  -", True, self.BLACK)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("4", True, self.BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.menu_position[3] == 3 and self.n == 3:
            text4 = font1.render("-  8  -", True, self.BLACK)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.menu_position[3] != 3 and self.n == 3:
            text4 = font.render("8", True, self.BLACK)
            txt4 = 1
#------------------------------------------------------------------------------------------------------------------------------------#        
        #PROMIEN PILKI
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.menu_position[3] == 0 and self.n == 3:
            text = font1.render("-  25  -", True, self.BLACK)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("25", True, self.BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font1.render("-  10  -", True, self.BLACK)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("10", True, self.BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font1.render("-  40  -", True, self.BLACK)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("40", True, self.BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.menu_position[3] == 3 and self.n == 3:
            text4 = font1.render("-  50  -", True, self.BLACK)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.menu_position[3] != 3 and self.n == 3:
            text4 = font.render("50", True, self.BLACK)
            txt4 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
#MENU ---> USTAWIENIA ---> SIATKA
        #WYSOKOSC SIATKI
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.menu_position[3] == 0 and self.n == 3:
            text = font1.render("-  300  -", True, self.BLACK)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("300", True, self.BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font1.render("-  250  -", True, self.BLACK)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("250", True, self.BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font1.render("-  350  -", True, self.BLACK)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("350", True, self.BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.menu_position[3] == 3 and self.n == 3:
            text4 = font1.render("-  400  -", True, self.BLACK)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.menu_position[3] != 3 and self.n == 3:
            text4 = font.render("400", True, self.BLACK)
            txt4 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #SZEROKOSC SIATKI
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.menu_position[3] == 0 and self.n == 3:
            text = font1.render("-  60  -", True, self.BLACK)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("60", True, self.BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font1.render("-  20  -", True, self.BLACK)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("20", True, self.BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font1.render("-  40  -", True, self.BLACK)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("40", True, self.BLACK)
            txt3 = 3
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.menu_position[3] == 3 and self.n == 3:
            text4 = font1.render("-  80  -", True, self.BLACK)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.menu_position[3] != 3 and self.n == 3:
            text4 = font.render("80", True, self.BLACK)
            txt4 = 1 
#WYSWIETLANIE TEKSTU        
        if txt1:
            textRect = text.get_rect()
            textRect.center = (self.WIDTH/2, 250*self.mnoznik_obiektow)
            self.screen.blit(text, textRect)
        if txt2:
            textRect2 = text2.get_rect()
            textRect2.center = (self.WIDTH/2, 300*self.mnoznik_obiektow)
            self.screen.blit(text2, textRect2)     
        if txt3:
            textRect3 = text3.get_rect()
            textRect3.center = (self.WIDTH/2, 350*self.mnoznik_obiektow)
            self.screen.blit(text3, textRect3)
        if txt4:
            textRect4 = text4.get_rect()
            textRect4.center = (self.WIDTH/2, 400*self.mnoznik_obiektow)
            self.screen.blit(text4, textRect4)
        if txt5:
            textRect5 = text5.get_rect()
            textRect5.center = (self.WIDTH/2, 450*self.mnoznik_obiektow)
            self.screen.blit(text5, textRect5)
        if txt6:
            textRect6 = text6.get_rect()
            textRect6.center = (self.WIDTH/2, 500*self.mnoznik_obiektow)
            self.screen.blit(text6, textRect6)
        #if txt7:
        #    textRect7 = text7.get_rect()
        #    textRect7.center = (self.WIDTH/2, 600*self.mnoznik_obiektow)
        #    self.screen.blit(text7, textRect7)
        self.odczyt()
        if self.txt7 and not txt6:
            textRect7 = self.text7.get_rect()
            textRect7.center = (self.WIDTH/2, 500*self.mnoznik_obiektow)
            self.screen.blit(self.text7, textRect7)
#OBECNY TYTUŁ - MAIN MENU
        text0_0 = font0_0.render("Error", True, BLACK)
        #MAIN MENU
        if self.n == 0:   
            text0_0 = font0_0.render("The Foxyball Game", True, BLACK)
        #USTAWIENIA
        if self.menu_position[0] == 1 and self.n == 1:
            text0_0 = font0_0.render("USTAWIENIA", True, BLACK)
        #STEROWANIE
        if self.menu_position[0] == 2 and self.n == 1:
            text0_0 = font0_0.render("STEROWANIE", True, BLACK)
        #AUTOR
        if self.menu_position[0] == 3 and self.n == 1:
            text0_0 = font0_0.render("AUTOR", True, BLACK)
#OBECNY TYTUŁ - USTAWIENIA
        #ROZMIAR I PREDKOSC GRACZY
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.n == 2:
            text0_0 = font0_0.render("ROZMIAR I PREDKOSC GRACZY", True, BLACK)
        #WIELKOSC OKNA
        if self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.n == 2:
            text0_0 = font0_0.render("WIELKOSC OKNA (zmiana powoduje reset gry)", True, BLACK)
        #FIZYKA
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.n == 2:
            text0_0 = font0_0.render("FIZYKA", True, BLACK)
        #PUNKTACJA
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.n == 2:
            text0_0 = font0_0.render("PUNKTACJA", True, BLACK)
        #PILKA
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.n == 2:
            text0_0 = font0_0.render("PILKA", True, BLACK)
        #SIATKA
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.n == 2:
            text0_0 = font0_0.render("SIATKA", True, BLACK)
#OBECNY TYTUŁ - ROZMIAR I PREDKOSC GRACZY
        #SZEROKOSC I WYSOKOSC GRACZY
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.n == 3:
            text0_0 = font0_0.render("SZEROKOSC I WYSOKOSC GRACZY", True, BLACK)
        #PREDKOSC SKOKU
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.n == 3:
            text0_0 = font0_0.render("PREDKOSC SKOKU", True, BLACK)
        #PREDKOSC PORUSZANIA SIE
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.n == 3:
            text0_0 = font0_0.render("PREDKOSC PORUSZANIA SIE", True, BLACK)
#OBECNY TYTUŁ - FIZYKA
        #STALA GRAWITACJI
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.n == 3:
            text0_0 = font0_0.render("STALA GRAWITACJI", True, BLACK)
        #PREDKOSC CZASU
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.n == 3:
            text0_0 = font0_0.render("PREDKOSC CZASU", True, BLACK)
#OBECNY TYTUŁ - PUNKTACJA
        #MAX DOZWOLONYCH ODBIC
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.n == 3:
            text0_0 = font0_0.render("MAX DOZWOLONYCH ODBIC", True, BLACK)
        #ILOSC RUND
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.n == 3:
            text0_0 = font0_0.render("ILOSC RUND", True, BLACK)
#OBECNY TYTUŁ - PILKA
        #PREDKOSC Y ODBICIA PILKI PRZEZ GRACZA
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.n == 3:
            text0_0 = font0_0.render("PREDKOSC Y ODBICIA PILKI PRZEZ GRACZA", True, BLACK)
        #PREDKOSC Y ODBICIA PILKI OD SIATKI
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.n == 3:
            text0_0 = font0_0.render("PREDKOSC Y ODBICIA PILKI OD SIATKI", True, BLACK)
        #PREDKOSC X PILKI
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.n == 3:
            text0_0 = font0_0.render("PREDKOSC X PILKI", True, BLACK)
        #PROMIEN PILKI
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.n == 3:
            text0_0 = font0_0.render("PROMIEN PILKI", True, BLACK)
#OBECNY TYTUŁ - SIATKA
        #WYSOKOSC SIATKI
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.n == 3:
            text0_0 = font0_0.render("WYSOKOSC SIATKI", True, BLACK)
        #SZEROKOSC SIATKI
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.n == 3:
            text0_0 = font0_0.render("SZEROKOSC SIATKI", True, BLACK)
#OBECY TYTUŁ + HINTY        
        textRect0_0 = text0_0.get_rect()
        textRect0_0.center = (self.WIDTH/2, 150*self.mnoznik_obiektow)
        self.screen.blit(text0_0, textRect0_0)

        text8 = font2.render("nacisnij 'q', zeby pojsc wstecz", True, BLACK)
        textRect8 = text8.get_rect()
        self.screen.blit(text8, [50, ((self.HEIGHT-textRect8.height)-50)])

        text9 = font2.render("nacisnij 'enter', zeby pojsc dalej/zmienic wartosc", True, BLACK)
        textRect9 = text9.get_rect()
        self.screen.blit(text9, [((self.WIDTH-textRect9.width)-50), ((self.HEIGHT-textRect9.height)-50)])
#------------------------------------------------------------------------------------------------------------------------------------#
    def odczyt_klawiszy(self):
        klawiatura = pygame.key.get_pressed()
        if klawiatura[pygame.K_LEFT] or klawiatura[pygame.K_a] or klawiatura[pygame.K_j]:
            pass
        if klawiatura[pygame.K_RIGHT] or klawiatura[pygame.K_d] or klawiatura[pygame.K_l]:
            pass
#ILOSC ELEMENTOW W MENU (W GORE)
        if klawiatura[pygame.K_UP] or klawiatura[pygame.K_w] or klawiatura[pygame.K_i]:
            #MAIN MENU
            if self.n == 0:
                if self.menu_position[self.n] == 0:
                    self.menu_position[self.n] = 3
                    self.dzwiek_zmiana.play()
                else:
                    self.menu_position[self.n] -= 1
                    self.dzwiek_zmiana.play()
            #USTAWIENIA
            elif self.menu_position[0] == 1 and self.n == 1:
                if self.menu_position[self.n] == 0:
                    self.menu_position[self.n] = 5
                    self.dzwiek_zmiana.play()
                else:
                    self.menu_position[self.n] -= 1
                    self.dzwiek_zmiana.play()
            #GRACZE
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.n == 2:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 2
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] -= 1
                   self.dzwiek_zmiana.play()
            #WIELKOSC EKRANU OPCJE
            elif self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.n == 2:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 2
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] -= 1
                   self.dzwiek_zmiana.play()
            #FIZYKA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.n == 2:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 1
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] -= 1
                   self.dzwiek_zmiana.play()
            #PUNKTACJA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.n == 2:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 1
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] -= 1
                   self.dzwiek_zmiana.play()
            #PIŁKA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.n == 2:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 3
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] -= 1
                   self.dzwiek_zmiana.play()
            #SIATKA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.n == 2:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 1
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] -= 1
                   self.dzwiek_zmiana.play()
            #SZEROKOSC I WYSOKOSC GRACZY
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 3
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] -= 1
                   self.dzwiek_zmiana.play()
            #PREDKOSC SKOKU GRACZA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 2
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] -= 1
                   self.dzwiek_zmiana.play()
            #PREDKOSC PORUSZANIA SIE GRACZA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 2
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] -= 1
                   self.dzwiek_zmiana.play()
            #STALA GRAWITACJI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 2
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] -= 1
                   self.dzwiek_zmiana.play()
            #SZYBKOSC CZASU
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 3
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] -= 1
                   self.dzwiek_zmiana.play()
            #MAX DOZWOLONYCH ODBIC 
            elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 3
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] -= 1
                   self.dzwiek_zmiana.play()
            #ILOSC RUND
            elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 3
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] -= 1
                   self.dzwiek_zmiana.play()
            #PREDKOSC Y ODBICIA PILKI PRZEZ GRACZA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 3
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] -= 1
                   self.dzwiek_zmiana.play()
            #PREDKOSC Y ODBICIA PILKI OD SIATKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 3
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] -= 1
                   self.dzwiek_zmiana.play()
            #PREDKOSC X PILKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 3
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] -= 1
                   self.dzwiek_zmiana.play()
            #PROMIEN PILKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 3
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] -= 1
                   self.dzwiek_zmiana.play()
            #WYSOKOSC SIATKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 3
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] -= 1
                   self.dzwiek_zmiana.play()
            #SZEROKOSC SIATKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 3
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] -= 1
                   self.dzwiek_zmiana.play()
#ILOSC ELEMENTOW W MENU (W DÓŁ)
        if klawiatura[pygame.K_DOWN] or klawiatura[pygame.K_s] or klawiatura[pygame.K_k]:
            #MAIN MENU
            if self.n == 0:
                if self.menu_position[self.n] == 3:
                    self.menu_position[self.n] = 0
                    self.dzwiek_zmiana.play()
                else:
                    self.menu_position[self.n] += 1
                    self.dzwiek_zmiana.play()
            #USTAWIENIA
            elif self.menu_position[0] == 1 and self.n == 1:
                if self.menu_position[self.n] == 5:
                    self.menu_position[self.n] = 0
                    self.dzwiek_zmiana.play()
                else:
                    self.menu_position[self.n] += 1
                    self.dzwiek_zmiana.play()
            #GRACZE
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.n == 2:
               if self.menu_position[self.n] == 2:
                   self.menu_position[self.n] = 0
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] += 1
                   self.dzwiek_zmiana.play()
            #WIELKOSC OKNA OPCJE
            elif self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.n == 2:
               if self.menu_position[self.n] == 2:
                   self.menu_position[self.n] = 0
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] += 1
                   self.dzwiek_zmiana.play()
            #FIZYKA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.n == 2:
               if self.menu_position[self.n] == 1:
                   self.menu_position[self.n] = 0
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] += 1
                   self.dzwiek_zmiana.play()
            #PUNKTACJA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.n == 2:
               if self.menu_position[self.n] == 1:
                   self.menu_position[self.n] = 0
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] += 1
                   self.dzwiek_zmiana.play()
            #PIŁKA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.n == 2:
               if self.menu_position[self.n] == 3:
                   self.menu_position[self.n] = 0
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] += 1
                   self.dzwiek_zmiana.play()
            #SIATKA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.n == 2:
               if self.menu_position[self.n] == 1:
                   self.menu_position[self.n] = 0
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] += 1
                   self.dzwiek_zmiana.play()
            #SZEROKOSC I WYSOKOSC GRACZY
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.n == 3:
               if self.menu_position[self.n] == 3:
                   self.menu_position[self.n] = 0
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] += 1
                   self.dzwiek_zmiana.play()
            #PREDKOSC SKOKU GRACZA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.n == 3:
               if self.menu_position[self.n] == 2:
                   self.menu_position[self.n] = 0
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] += 1
                   self.dzwiek_zmiana.play()
            #PREDKOSC PORUSZANIA SIE GRACZA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.n == 3:
               if self.menu_position[self.n] == 2:
                   self.menu_position[self.n] = 0
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] += 1
                   self.dzwiek_zmiana.play()
            #STALA GRAWITACJI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.n == 3:
               if self.menu_position[self.n] == 2:
                   self.menu_position[self.n] = 0
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] += 1
                   self.dzwiek_zmiana.play()
            #SZYBKOSC CZASU
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.n == 3:
               if self.menu_position[self.n] == 3:
                   self.menu_position[self.n] = 0
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] += 1
                   self.dzwiek_zmiana.play()
            #MAX DOZWOLONYCH ODBIC 
            elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.n == 3:
               if self.menu_position[self.n] == 3:
                   self.menu_position[self.n] = 0
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] += 1
                   self.dzwiek_zmiana.play()
            #ILOSC RUND
            elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.n == 3:
               if self.menu_position[self.n] == 3:
                   self.menu_position[self.n] = 0
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] += 1
                   self.dzwiek_zmiana.play()
            #PREDKOSC Y ODBICIA PILKI PRZEZ GRACZA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.n == 3:
               if self.menu_position[self.n] == 3:
                   self.menu_position[self.n] = 0
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] += 1
                   self.dzwiek_zmiana.play()
            #PREDKOSC Y ODBICIA PILKI OD SIATKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.n == 3:
               if self.menu_position[self.n] == 3:
                   self.menu_position[self.n] = 0
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] += 1
                   self.dzwiek_zmiana.play()
            #PREDKOSC X PILKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.n == 3:
               if self.menu_position[self.n] == 3:
                   self.menu_position[self.n] = 0
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] += 1
                   self.dzwiek_zmiana.play()
            #PROMIEN PILKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.n == 3:
               if self.menu_position[self.n] == 3:
                   self.menu_position[self.n] = 0
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] += 1
                   self.dzwiek_zmiana.play()
            #WYSOKOSC SIATKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.n == 3:
               if self.menu_position[self.n] == 3:
                   self.menu_position[self.n] = 0
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] += 1
                   self.dzwiek_zmiana.play()
            #SZEROKOSC SIATKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.n == 3:
               if self.menu_position[self.n] == 3:
                   self.menu_position[self.n] = 0
                   self.dzwiek_zmiana.play()
               else:
                   self.menu_position[self.n] += 1
                   self.dzwiek_zmiana.play()
#ZAPIS WARTOSCI            
        if klawiatura[pygame.K_RETURN]:
            self.dzwiek_enter.play()
            if self.menu_position[0] == 0:
                #WŁACZA SIE GRA
                self.menu_time = False
            elif self.menu_position[0] == 2 and self.n == 1:
                pass
            elif self.menu_position[0] == 3 and self.n == 1:
                pass

            #WIELKOSC OKNA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.menu_position[2] == 0 and self.n == 2:
                self.zapis_do_pliku(4, 1280)
                self.zapis_do_pliku(5, 720)
                self.dzwiek_wroc.play()
                pygame.time.wait(500)
                pygame.quit()
                sys.exit()
            elif self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.menu_position[2] == 1 and self.n == 2:
                self.zapis_do_pliku(4, 1600)
                self.zapis_do_pliku(5, 900)
                self.dzwiek_wroc.play()
                pygame.time.wait(500)
                pygame.quit()
                sys.exit()
            elif self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.menu_position[2] == 2 and self.n == 2:
                self.zapis_do_pliku(4, 1920)
                self.zapis_do_pliku(5, 1080)
                self.dzwiek_wroc.play()
                pygame.time.wait(500)
                pygame.quit()
                sys.exit()
                     
            #SZEROKOSC I WYSOKOSC GRACZY
            #elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] == 0 and self.n == 3:
            #    self.zapis_do_pliku(1, 100)
            #    self.zapis_do_pliku(2, 50)
            #elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] == 1 and self.n == 3:
            #    self.zapis_do_pliku(1, 150)
            #    self.zapis_do_pliku(2, 75)
            #elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] == 2 and self.n == 3:
            #    self.zapis_do_pliku(1, 200)
            #    self.zapis_do_pliku(2, 100)
            
            #SZEROKOSC I WYSOKOSC GRACZY
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] == 0 and self.n == 3:
                self.zapis_do_pliku(1, 200)
                self.zapis_do_pliku(2, 100)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] == 1 and self.n == 3:
                self.zapis_do_pliku(1, 100)
                self.zapis_do_pliku(2, 50)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] == 2 and self.n == 3:
                self.zapis_do_pliku(1, 170)
                self.zapis_do_pliku(2, 85)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] == 3 and self.n == 3:
                self.zapis_do_pliku(1, 230)
                self.zapis_do_pliku(2, 115)
            
            #PREDKOSC SKOKU GRACZA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.menu_position[3] == 0 and self.n == 3:
                self.zapis_do_pliku(10, -60)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.menu_position[3] == 1 and self.n == 3:
                self.zapis_do_pliku(10, -40)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.menu_position[3] == 2 and self.n == 3:
                self.zapis_do_pliku(10, -80)
            
            #PREDKOSC PORUSZANIA SIE GRACZA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.menu_position[3] == 0 and self.n == 3:
                self.zapis_do_pliku(11, 40)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.menu_position[3] == 1 and self.n == 3:
                self.zapis_do_pliku(11, 60)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.menu_position[3] == 2 and self.n == 3:
                self.zapis_do_pliku(11, 80)
            
            #STALA GRAWITACJI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.menu_position[3] == 0 and self.n == 3:
                self.zapis_do_pliku(7, 9.81)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.menu_position[3] == 1 and self.n == 3:
                self.zapis_do_pliku(7, 13.81)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.menu_position[3] == 2 and self.n == 3:
                self.zapis_do_pliku(7, 5.81)
            
            #SZYBKOSC CZASU
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] == 0 and self.n == 3:
                self.zapis_do_pliku(8, 0.20)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] == 1 and self.n == 3:
                self.zapis_do_pliku(8, 0.10)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] == 2 and self.n == 3:
                self.zapis_do_pliku(8, 0.25)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] == 3 and self.n == 3:
                self.zapis_do_pliku(8, 0.30)
            
            #MAX DOZWOLONYCH ODBIC
            elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.menu_position[3] == 0 and self.n == 3:
                self.zapis_do_pliku(13, 3)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.menu_position[3] == 1 and self.n == 3:
                self.zapis_do_pliku(13, 1)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.menu_position[3] == 2 and self.n == 3:
                self.zapis_do_pliku(13, 5)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.menu_position[3] == 3 and self.n == 3:
                self.zapis_do_pliku(13, 100)

            #ILOSC RUND
            elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.menu_position[3] == 0 and self.n == 3:
                self.zapis_do_pliku(14, 5)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.menu_position[3] == 1 and self.n == 3:
                self.zapis_do_pliku(14, 1)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.menu_position[3] == 2 and self.n == 3:
                self.zapis_do_pliku(14, 10)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.menu_position[3] == 3 and self.n == 3:
                self.zapis_do_pliku(14, 15)
            
            #PREDKOSC Y ODBICIA PILKI PRZEZ GRACZA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.menu_position[3] == 0 and self.n == 3:
                self.zapis_do_pliku(16, -80)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.menu_position[3] == 1 and self.n == 3:
                self.zapis_do_pliku(16, -40)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.menu_position[3] == 2 and self.n == 3:
                self.zapis_do_pliku(16, -60)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.menu_position[3] == 3 and self.n == 3:
                self.zapis_do_pliku(16, -100)
            
            #PREDKOSC Y ODBICIA PILKI OD GRACZA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.menu_position[3] == 0 and self.n == 3:
                self.zapis_do_pliku(17, -40)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.menu_position[3] == 1 and self.n == 3:
                self.zapis_do_pliku(17, -20)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.menu_position[3] == 2 and self.n == 3:
                self.zapis_do_pliku(17, -60)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.menu_position[3] == 3 and self.n == 3:
                self.zapis_do_pliku(17, -80)

            #PREDKOSC X PILKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.menu_position[3] == 0 and self.n == 3:
                self.zapis_do_pliku(18, 6)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.menu_position[3] == 1 and self.n == 3:
                self.zapis_do_pliku(18, 2)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.menu_position[3] == 2 and self.n == 3:
                self.zapis_do_pliku(18, 4)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.menu_position[3] == 3 and self.n == 3:
                self.zapis_do_pliku(18, 8)
            
            #PROMIEN PILKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.menu_position[3] == 0 and self.n == 3:
                self.zapis_do_pliku(19, 25)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.menu_position[3] == 1 and self.n == 3:
                self.zapis_do_pliku(19, 10)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.menu_position[3] == 2 and self.n == 3:
                self.zapis_do_pliku(19, 40)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.menu_position[3] == 3 and self.n == 3:
                self.zapis_do_pliku(19, 50)
            
            #WYSOKOSC SIATKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.menu_position[3] == 0 and self.n == 3:
                self.zapis_do_pliku(21, 300)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.menu_position[3] == 1 and self.n == 3:
                self.zapis_do_pliku(21, 250)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.menu_position[3] == 2 and self.n == 3:
                self.zapis_do_pliku(21, 350)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.menu_position[3] == 3 and self.n == 3:
                self.zapis_do_pliku(21, 400)
            
            #SZEROKOSC SIATKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.menu_position[3] == 0 and self.n == 3:
                self.zapis_do_pliku(22, 60)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.menu_position[3] == 1 and self.n == 3:
                self.zapis_do_pliku(22, 20)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.menu_position[3] == 2 and self.n == 3:
                self.zapis_do_pliku(22, 40)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.menu_position[3] == 3 and self.n == 3:
                self.zapis_do_pliku(22, 80)
#------------------------------------------------------------------------------------------------------------------------------------#
            #WYCHODZENIE POZA ZAKRES
            elif self.n == 3:
                pass
            else:
                self.n += 1
            
        if klawiatura[pygame.K_q]:
            #WYCHODZENIE POZA ZAKRES
            if self.n == 0:
                pass
            else:
                self.dzwiek_wroc.play()
                self.menu_position[self.n] = 0
                self.n -= 1
#ZAPIS DO PLIKU
    def zapis_do_pliku(self, numer_lini, wartosc):
        current_path = os.getcwd()
        path = current_path+'/settings/parameters.txt'
        #print(path)
        with open(path, 'r') as plik:
            data = plik.readlines()
        #NADPISANIE KONKRETNEJ LINI
        if type(wartosc) is int:
            data[numer_lini] = '%d\n' % (wartosc)
        if type(wartosc) is float:
            data[numer_lini] = '%.2f\n' % (wartosc)
        #print(type(wartosc))
        #ZAPIS Z NOWYMI WARTOSCIAMI
        with open(path, 'w') as plik:
            plik.writelines(data)
        plik.close()
#OBECNA WARTOSC:
    def odczyt(self):
        ans = 0
        num = 0
        #WIELKOSC EKRANU OPCJE
        if self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.n == 2:
            num = 4
        #SZEROKOSC I WYSOKOSC GRACZY
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.n == 3:
            num = 1
        #PREDKOSC SKOKU GRACZA
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.n == 3:
            num = 10
        #PREDKOSC PORUSZANIA SIE GRACZA
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.n == 3:
            num = 11
        #STALA GRAWITACJI
        elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.n == 3:
            num = 7
        #SZYBKOSC CZASU
        elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.n == 3:
            num = 8
        #MAX DOZWOLONYCH ODBIC 
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.n == 3:
            num = 13
        #ILOSC RUND
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.n == 3:
            num = 14
        #PREDKOSC Y ODBICIA PILKI PRZEZ GRACZA
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.n == 3:
            num = 16
        #PREDKOSC Y ODBICIA PILKI OD SIATKI
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.n == 3:
            num = 17
        #PREDKOSC X PILKI
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.n == 3:
            num = 18
        #PROMIEN PILKI
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.n == 3:
            num = 19
        #WYSOKOSC SIATKI
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.n == 3:
            num = 21
        #SZEROKOSC SIATKI
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.n == 3:
            num = 22
        else:
            num = 0
#WYSWIETLENIE OBECNEJ WARTOSCI:
        if num == 1 or num == 4:
            self.text7 = font_1.render("OBECNIE: %dx%d" % (self.odczyt_z_pliku(num), self.odczyt_z_pliku(num+1)), True, self.BLACK)
            self.txt7 = 1
        elif num == 7 or num == 8:
            self.text7 = font_1.render("OBECNIE: %.2f" % (self.odczyt_z_pliku(num)), True, self.BLACK)
            self.txt7 = 1
        elif num != 0:
            self.text7 = font_1.render("OBECNIE: %d" % (self.odczyt_z_pliku(num)), True, self.BLACK)
            self.txt7 = 1
        else:
            self.txt7 = 0      
#ODCZYT Z PLIKU OBECNEJ WARTOSCI:    
    def odczyt_z_pliku(self, number):
        current_path = os.getcwd()
        path = current_path+'/settings/parameters.txt'
        with open(path, 'r') as plik:
            data = plik.readlines()
        try:
            ans = int(data[number])
            if ans < 0:
                ans *= -1
        except:
            ans = float(data[number])
        plik.close()
        return ans


menu()