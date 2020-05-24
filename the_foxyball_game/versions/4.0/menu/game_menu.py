import pygame, sys, os
from settings.settings import settings

WIDTH = settings().WIDTH
HEIGHT = settings().HEIGHT
BLACK = settings().BLACK
WHITE = settings().WHITE
GREEN = settings().GREEN
GRAY = settings().GRAY
RED = settings().RED
ORANGE = settings().ORANGE
pygame.init()
font0 = pygame.font.Font('fonts/ostrich-regular.ttf', 78)
font0_0 = pygame.font.Font('fonts/ostrich-heavy.otf', 78)
font = pygame.font.Font('fonts/ostrich-regular.ttf', 42)
font1 = pygame.font.Font('fonts/ostrich-regular.ttf', 56)
font2 = pygame.font.Font('fonts/ostrich-regular.ttf', 28)


class menu(object):

    def __init__(self):
        pygame.mixer.music.load('music/menu_music.mp3')
        pygame.mixer.music.play(-1)
        self.max_fps = 60.0
        self.n = 0
        self.menu_position = [0,0,0,0]
        self.mnoznik_obiektow = settings().mnoznik_obiektow

        #SCREEN
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('The Foxyball Game')
        self.background = pygame.transform.scale(pygame.image.load('textures/background.png'), (WIDTH, HEIGHT))

        #PĘTLA
        self.menu_time = True
        while self.menu_time:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
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
        txt7 = 0

        if self.menu_position[0] == 0 and self.n == 0:
            text = font1.render("-  GRAJ  -", True, BLACK)
            txt1 = 1
        elif self.menu_position[0] != 0 and self.n == 0:
            text = font.render("GRAJ", True, BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.n == 0:
            text2 = font1.render("-  USTAWIENIA  -", True, BLACK)
            txt2 = 1
        elif self.menu_position[0] != 1 and self.n == 0:
            text2 = font.render("USTAWIENIA", True, BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 2 and self.n == 0:
            text3 = font1.render("-  STEROWANIE  -", True, BLACK)
            txt3 = 1
        elif self.menu_position[0] != 2 and self.n == 0:
            text3 = font.render("STEROWANIE", True, BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 3 and self.n == 0:
            text4 = font1.render("-  AUTOR  -", True, BLACK)
            txt4 = 1
        elif self.menu_position[0] != 3 and self.n == 0:
            text4 = font.render("AUTOR", True, BLACK)
            txt4 = 1
        
        #if self.menu_position[self.n] == 6:
        #    text7 = font.render("numeracja menu: (%d, %d, %d, %d) n: %d" % (self.menu_position[0], self.menu_position[1], self.menu_position[2], self.menu_position[3], self.n), True, BLACK, WHITE)
        #    txt7 = 1
        #elif self.menu_position[self.n] != 6:
        #    text7 = font.render("numeracja menu: (%d, %d, %d, %d) n: %d" % (self.menu_position[0], self.menu_position[1], self.menu_position[2], self.menu_position[3], self.n), True, WHITE, BLACK)
        #    txt7 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #USTAWIENIA
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.n == 1:
            text = font.render("ROZMIAR I PREDKOSC GRACZY", True, BLACK, WHITE)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] != 0 and self.n == 1:
            text = font.render("ROZMIAR I PREDKOSC GRACZY", True, WHITE, BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.n == 1:
            text2 = font.render("WIELKOSC OKNA", True, BLACK, WHITE)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] != 1 and self.n == 1:
            text2 = font.render("WIELKOSC OKNA", True, WHITE, BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.n == 1:
            text3 = font.render("FIZYKA", True, BLACK, WHITE)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] != 2 and self.n == 1:
            text3 = font.render("FIZYKA", True, WHITE, BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.n == 1:
            text4 = font.render("PUNKTACJA", True, BLACK, WHITE)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] != 3 and self.n == 1:
            text4 = font.render("PUNKTACJA", True, WHITE, BLACK)
            txt4 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.n == 1:
            text5 = font.render("PILKA", True, BLACK, WHITE)
            txt5 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] != 4 and self.n == 1:
            text5 = font.render("PILKA", True, WHITE, BLACK)
            txt5 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.n == 1:
            text6 = font.render("SIATKA", True, BLACK, WHITE)
            txt6 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] != 5 and self.n == 1:
            text6 = font.render("SIATKA", True, WHITE, BLACK)
            txt6 = 1
#------------------------------------------------------------------------------------------------------------------------------------#                
        #STEROWANIE
        if self.menu_position[0] == 2 and self.n == 1:
            sterowanie_txt1 = 'GRACZ 1: "W"-skok  "A"-krok w lewo  "D"-krok w prawo'
            text = font.render(sterowanie_txt1, True, WHITE, BLACK)
            sterowanie_txt2 = 'GRACZ 2: "I"-skok  "J"-krok w lewo  "L"-krok w prawo'
            text2 = font.render(sterowanie_txt2, True, WHITE, BLACK)
            sterowanie_txt3 = "Klawisz 'Esc' powoduje wyjscie z gry"
            text3 = font.render(sterowanie_txt3, True, WHITE, BLACK)
            txt1 = 1
            txt2 = 1
            txt3 = 1
#------------------------------------------------------------------------------------------------------------------------------------#                
        #AUTOR
        if self.menu_position[0] == 3 and self.n == 1:
            text = font.render("Karol Bolanowski, ISSP rok 1", True, WHITE, BLACK)
            txt1 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
#MENU ---> USTAWIENIA
        #ROZMIAR I PRĘDKOSC GRACZY
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.n == 2:
            text = font.render("SZEROKOSC I WYSOKOSC GRACZY", True, BLACK, WHITE)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] != 0 and self.n == 2:
            text = font.render("SZEROKOSC I WYSOKOSC GRACZY", True, WHITE, BLACK)
            txt1 = 1
        
        #if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.n == 2:
        #    text2 = font.render("WYSOKOSC GRACZY", True, BLACK, WHITE)
        #    txt2 = 1
        #elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] != 1 and self.n == 2:
        #    text2 = font.render("WYSOKOSC GRACZY", True, WHITE, BLACK)
        #    txt2 = 1

        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.n == 2:
            text2 = font.render("PREDKOSC SKOKU", True, BLACK, WHITE)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] != 1 and self.n == 2:
            text2 = font.render("PREDKOSC SKOKU", True, WHITE, BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.n == 2:
            text3 = font.render("PREDKOSC PORUSZANIA SIE", True, BLACK, WHITE)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] != 2 and self.n == 2:
            text3 = font.render("PREDKOSC PORUSZANIA SIE", True, WHITE, BLACK)
            txt3 = 1
#------------------------------------------------------------------------------------------------------------------------------------#                
        #WIELKOSC OKNA:
        if self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.menu_position[2] == 0 and self.n == 2:
            text = font.render("1280x720", True, BLACK, WHITE)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.menu_position[2] != 0 and self.n == 2:
            text = font.render("1280x720", True, WHITE, BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.menu_position[2] == 1 and self.n == 2:
            text2 = font.render("1366x768", True, BLACK, WHITE)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.menu_position[2] != 1 and self.n == 2:
            text2 = font.render("1366x768", True, WHITE, BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.menu_position[2] == 2 and self.n == 2:
            text3 = font.render("1920x1080", True, BLACK, WHITE)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.menu_position[2] != 2 and self.n == 2:
            text3 = font.render("1920x1080", True, WHITE, BLACK)
            txt3 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #FIZYKA:
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.n == 2:
            text = font.render("STALA GRAWITACJI", True, BLACK, WHITE)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] != 0 and self.n == 2:
            text = font.render("STALA GRAWITACJI", True, WHITE, BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.n == 2:
            text2 = font.render("SZYBKOSC CZASU", True, BLACK, WHITE)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] != 1 and self.n == 2:
            text2 = font.render("SZYBKOSC CZASU", True, WHITE, BLACK)
            txt2 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #PUNKTACJA:
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.n == 2:
            text = font.render("MAX DOZWOLONYCH ODBIC", True, BLACK, WHITE)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] != 0 and self.n == 2:
            text = font.render("MAX DOZWOLONYCH ODBIC", True, WHITE, BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.n == 2:
            text2 = font.render("ILOSC RUND", True, BLACK, WHITE)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] != 1 and self.n == 2:
            text2 = font.render("ILOSC RUND", True, WHITE, BLACK)
            txt2 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #PIŁKA:
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.n == 2:
            text = font.render("PREDKOSC Y ODBICIA PILKI PRZEZ GRACZA", True, BLACK, WHITE)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] != 0 and self.n == 2:
            text = font.render("PREDKOSC Y ODBICIA PILKI PRZEZ GRACZA", True, WHITE, BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.n == 2:
            text2 = font.render("PREDKOSC Y ODBICIA PILKI OD SIATKI", True, BLACK, WHITE)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] != 1 and self.n == 2:
            text2 = font.render("PREDKOSC Y ODBICIA PILKI OD SIATKI", True, WHITE, BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.n == 2:
            text3 = font.render("PREDKOSC X PILKI", True, BLACK, WHITE)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] != 2 and self.n == 2:
            text3 = font.render("PREDKOSC X PILKI", True, WHITE, BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.n == 2:
            text4 = font.render("PROMIEN PILKI", True, BLACK, WHITE)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] != 3 and self.n == 2:
            text4 = font.render("PROMIEN PILKI", True, WHITE, BLACK)
            txt4 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #SIATKA:
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.n == 2:
            text = font.render("WYSOKOSC SIATKI", True, BLACK, WHITE)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] != 0 and self.n == 2:
            text = font.render("WYSOKOSC SIATKI", True, WHITE, BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.n == 2:
            text2 = font.render("SZEROKOSC SIATKI", True, BLACK, WHITE)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] != 1 and self.n == 2:
            text2 = font.render("SZEROKOSC SIATKI", True, WHITE, BLACK)
            txt2 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
#MENU ---> USTAWIENIA ---> ROZMIAR I PREDKOSC GRACZY
        #SZEROKOSC I WYSOKOSC GRACZY
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] == 0 and self.n == 3:
            text = font.render("100x50", True, BLACK, WHITE)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("100x50", True, WHITE, BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font.render("150x75", True, BLACK, WHITE)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("150x75", True, WHITE, BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font.render("200x100", True, BLACK, WHITE)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("200x100", True, WHITE, BLACK)
            txt3 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #PREDKOSC SKOKU GRACZA
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.menu_position[3] == 0 and self.n == 3:
            text = font.render("60", True, BLACK, WHITE)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("60", True, WHITE, BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font.render("40", True, BLACK, WHITE)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("40", True, WHITE, BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font.render("80", True, BLACK, WHITE)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("80", True, WHITE, BLACK)
            txt3 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #PREDKOSC PORUSZANIA SIE GRACZA
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.menu_position[3] == 0 and self.n == 3:
            text = font.render("40", True, BLACK, WHITE)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("40", True, WHITE, BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font.render("60", True, BLACK, WHITE)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("60", True, WHITE, BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font.render("80", True, BLACK, WHITE)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("80", True, WHITE, BLACK)
            txt3 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
#MENU ---> USTAWIENIA ---> FIZYKA
        #STALA GRAWITACJI
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.menu_position[3] == 0 and self.n == 3:
            text = font.render("9.81", True, BLACK, WHITE)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("9.81", True, WHITE, BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font.render("12.0", True, BLACK, WHITE)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("12.0", True, WHITE, BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font.render("8.0", True, BLACK, WHITE)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("8.0", True, WHITE, BLACK)
            txt3 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #SZYBKOSC CZASU
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] == 0 and self.n == 3:
            text = font.render("0.2", True, BLACK, WHITE)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("0.2", True, WHITE, BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font.render("0.1", True, BLACK, WHITE)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("0.1", True, WHITE, BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font.render("0.5", True, BLACK, WHITE)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("0.5", True, WHITE, BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] == 3 and self.n == 3:
            text4 = font.render("1.0", True, BLACK, WHITE)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] != 3 and self.n == 3:
            text4 = font.render("1.0", True, WHITE, BLACK)
            txt4 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
#MENU ---> USTAWIENIA ---> PUNKTACJA
        #MAX DOZWOLONYCH ODBIC
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.menu_position[3] == 0 and self.n == 3:
            text = font.render("3", True, BLACK, WHITE)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("3", True, WHITE, BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font.render("1", True, BLACK, WHITE)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("1", True, WHITE, BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font.render("5", True, BLACK, WHITE)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("5", True, WHITE, BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.menu_position[3] == 3 and self.n == 3:
            text4 = font.render("100", True, BLACK, WHITE)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.menu_position[3] != 3 and self.n == 3:
            text4 = font.render("100", True, WHITE, BLACK)
            txt4 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #ILOSC RUND
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.menu_position[3] == 0 and self.n == 3:
            text = font.render("5", True, BLACK, WHITE)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("5", True, WHITE, BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font.render("1", True, BLACK, WHITE)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("1", True, WHITE, BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font.render("10", True, BLACK, WHITE)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("10", True, WHITE, BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.menu_position[3] == 3 and self.n == 3:
            text4 = font.render("15", True, BLACK, WHITE)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.menu_position[3] != 3 and self.n == 3:
            text4 = font.render("15", True, WHITE, BLACK)
            txt4 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
#MENU ---> USTAWIENIA ---> PIŁKA
        #PREDKOSC Y ODBICIA PILKI PRZEZ GRACZA
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.menu_position[3] == 0 and self.n == 3:
            text = font.render("80", True, BLACK, WHITE)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("80", True, WHITE, BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font.render("40", True, BLACK, WHITE)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("40", True, WHITE, BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font.render("60", True, BLACK, WHITE)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("60", True, WHITE, BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.menu_position[3] == 3 and self.n == 3:
            text4 = font.render("100", True, BLACK, WHITE)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.menu_position[3] != 3 and self.n == 3:
            text4 = font.render("100", True, WHITE, BLACK)
            txt4 = 1
#------------------------------------------------------------------------------------------------------------------------------------#      
        #PREDKOSC Y ODBICIA PILKI OD SIATKI
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.menu_position[3] == 0 and self.n == 3:
            text = font.render("40", True, BLACK, WHITE)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("40", True, WHITE, BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font.render("20", True, BLACK, WHITE)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("20", True, WHITE, BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font.render("60", True, BLACK, WHITE)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("60", True, WHITE, BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.menu_position[3] == 3 and self.n == 3:
            text4 = font.render("80", True, BLACK, WHITE)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.menu_position[3] != 3 and self.n == 3:
            text4 = font.render("80", True, WHITE, BLACK)
            txt4 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #PREDKOSC X PILKI
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.menu_position[3] == 0 and self.n == 3:
            text = font.render("6", True, BLACK, WHITE)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("6", True, WHITE, BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font.render("2", True, BLACK, WHITE)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("2", True, WHITE, BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font.render("4", True, BLACK, WHITE)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("4", True, WHITE, BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.menu_position[3] == 3 and self.n == 3:
            text4 = font.render("8", True, BLACK, WHITE)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.menu_position[3] != 3 and self.n == 3:
            text4 = font.render("8", True, WHITE, BLACK)
            txt4 = 1
#------------------------------------------------------------------------------------------------------------------------------------#        
        #PROMIEN PILKI
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.menu_position[3] == 0 and self.n == 3:
            text = font.render("25", True, BLACK, WHITE)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("25", True, WHITE, BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font.render("10", True, BLACK, WHITE)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("10", True, WHITE, BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font.render("40", True, BLACK, WHITE)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("40", True, WHITE, BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.menu_position[3] == 3 and self.n == 3:
            text4 = font.render("50", True, BLACK, WHITE)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.menu_position[3] != 3 and self.n == 3:
            text4 = font.render("50", True, WHITE, BLACK)
            txt4 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
#MENU ---> USTAWIENIA ---> SIATKA
        #WYSOKOSC SIATKI
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.menu_position[3] == 0 and self.n == 3:
            text = font.render("300", True, BLACK, WHITE)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("300", True, WHITE, BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font.render("250", True, BLACK, WHITE)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("250", True, WHITE, BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font.render("350", True, BLACK, WHITE)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("350", True, WHITE, BLACK)
            txt3 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.menu_position[3] == 3 and self.n == 3:
            text4 = font.render("400", True, BLACK, WHITE)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.menu_position[3] != 3 and self.n == 3:
            text4 = font.render("400", True, WHITE, BLACK)
            txt4 = 1
#------------------------------------------------------------------------------------------------------------------------------------#
        #SZEROKOSC SIATKI
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.menu_position[3] == 0 and self.n == 3:
            text = font.render("60", True, BLACK, WHITE)
            txt1 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.menu_position[3] != 0 and self.n == 3:
            text = font.render("60", True, WHITE, BLACK)
            txt1 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.menu_position[3] == 1 and self.n == 3:
            text2 = font.render("20", True, BLACK, WHITE)
            txt2 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.menu_position[3] != 1 and self.n == 3:
            text2 = font.render("20", True, WHITE, BLACK)
            txt2 = 1
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.menu_position[3] == 2 and self.n == 3:
            text3 = font.render("40", True, BLACK, WHITE)
            txt3 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.menu_position[3] != 2 and self.n == 3:
            text3 = font.render("40", True, WHITE, BLACK)
            txt3 = 3
        
        if self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.menu_position[3] == 3 and self.n == 3:
            text4 = font.render("80", True, BLACK, WHITE)
            txt4 = 1
        elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.menu_position[3] != 3 and self.n == 3:
            text4 = font.render("80", True, WHITE, BLACK)
            txt4 = 1 
#WYSWIETLANIE TEKSTU        
        if txt1:
            textRect = text.get_rect()
            textRect.center = (WIDTH/2, 300*self.mnoznik_obiektow)
            self.screen.blit(text, textRect)
        if txt2:
            textRect2 = text2.get_rect()
            textRect2.center = (WIDTH/2, 350*self.mnoznik_obiektow)
            self.screen.blit(text2, textRect2)     
        if txt3:
            textRect3 = text3.get_rect()
            textRect3.center = (WIDTH/2, 400*self.mnoznik_obiektow)
            self.screen.blit(text3, textRect3)
        if txt4:
            textRect4 = text4.get_rect()
            textRect4.center = (WIDTH/2, 450*self.mnoznik_obiektow)
            self.screen.blit(text4, textRect4)
        if txt5:
            textRect5 = text5.get_rect()
            textRect5.center = (WIDTH/2, 500*self.mnoznik_obiektow)
            self.screen.blit(text5, textRect5)
        if txt6:
            textRect6 = text6.get_rect()
            textRect6.center = (WIDTH/2, 550*self.mnoznik_obiektow)
            self.screen.blit(text6, textRect6)
        if txt7:
            textRect7 = text7.get_rect()
            textRect7.center = (WIDTH/2, 600*self.mnoznik_obiektow)
            self.screen.blit(text7, textRect7)
        
        text0_0 = font0_0.render("The Foxyball Game", True, BLACK)
        textRect0_0 = text0_0.get_rect()
        textRect0_0.center = (WIDTH/2, 150*self.mnoznik_obiektow)
        self.screen.blit(text0_0, textRect0_0)

        text8 = font2.render("nacisnij 'q' zeby pojsc wstecz", True, BLACK)
        textRect8 = text8.get_rect()
        self.screen.blit(text8, [50*self.mnoznik_obiektow, ((HEIGHT-textRect8.height)-50)*self.mnoznik_obiektow])

        text9 = font2.render("nacisnij 'enter' zeby pojsc dalej/zmienic wartosc", True, BLACK)
        textRect9 = text9.get_rect()
        self.screen.blit(text9, [((WIDTH-textRect9.width)-50)*self.mnoznik_obiektow, ((HEIGHT-textRect9.height)-50)*self.mnoznik_obiektow])
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
                else:
                    self.menu_position[self.n] -= 1
            #USTAWIENIA
            elif self.menu_position[0] == 1 and self.n == 1:
                if self.menu_position[self.n] == 0:
                    self.menu_position[self.n] = 5
                else:
                    self.menu_position[self.n] -= 1
            #GRACZE
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.n == 2:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 2
               else:
                   self.menu_position[self.n] -= 1
            #WIELKOSC EKRANU OPCJE
            elif self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.n == 2:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 2
               else:
                   self.menu_position[self.n] -= 1
            #FIZYKA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.n == 2:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 1
               else:
                   self.menu_position[self.n] -= 1
            #PUNKTACJA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.n == 2:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 1
               else:
                   self.menu_position[self.n] -= 1
            #PIŁKA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.n == 2:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 3
               else:
                   self.menu_position[self.n] -= 1
            #SIATKA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.n == 2:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 1
               else:
                   self.menu_position[self.n] -= 1
            #SZEROKOSC I WYSOKOSC GRACZY
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 2
               else:
                   self.menu_position[self.n] -= 1
            #PREDKOSC SKOKU GRACZA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 2
               else:
                   self.menu_position[self.n] -= 1
            #PREDKOSC PORUSZANIA SIE GRACZA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 2
               else:
                   self.menu_position[self.n] -= 1
            #STALA GRAWITACJI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 2
               else:
                   self.menu_position[self.n] -= 1
            #SZYBKOSC CZASU
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 3
               else:
                   self.menu_position[self.n] -= 1
            #MAX DOZWOLONYCH ODBIC 
            elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 3
               else:
                   self.menu_position[self.n] -= 1
            #ILOSC RUND
            elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 3
               else:
                   self.menu_position[self.n] -= 1
            #PREDKOSC Y ODBICIA PILKI PRZEZ GRACZA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 3
               else:
                   self.menu_position[self.n] -= 1
            #PREDKOSC Y ODBICIA PILKI OD SIATKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 3
               else:
                   self.menu_position[self.n] -= 1
            #PREDKOSC X PILKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 3
               else:
                   self.menu_position[self.n] -= 1
            #PROMIEN PILKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 3
               else:
                   self.menu_position[self.n] -= 1
            #WYSOKOSC SIATKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 3
               else:
                   self.menu_position[self.n] -= 1
            #SZEROKOSC SIATKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.n == 3:
               if self.menu_position[self.n] == 0:
                   self.menu_position[self.n] = 3
               else:
                   self.menu_position[self.n] -= 1
#ILOSC ELEMENTOW W MENU (W DÓŁ)
        if klawiatura[pygame.K_DOWN] or klawiatura[pygame.K_s] or klawiatura[pygame.K_k]:
            #MAIN MENU
            if self.n == 0:
                if self.menu_position[self.n] == 3:
                    self.menu_position[self.n] = 0
                else:
                    self.menu_position[self.n] += 1
            #USTAWIENIA
            elif self.menu_position[0] == 1 and self.n == 1:
                if self.menu_position[self.n] == 5:
                    self.menu_position[self.n] = 0
                else:
                    self.menu_position[self.n] += 1
            #GRACZE
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.n == 2:
               if self.menu_position[self.n] == 2:
                   self.menu_position[self.n] = 0
               else:
                   self.menu_position[self.n] += 1
            #WIELKOSC OKNA OPCJE
            elif self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.n == 2:
               if self.menu_position[self.n] == 2:
                   self.menu_position[self.n] = 0
               else:
                   self.menu_position[self.n] += 1
            #FIZYKA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.n == 2:
               if self.menu_position[self.n] == 1:
                   self.menu_position[self.n] = 0
               else:
                   self.menu_position[self.n] += 1
            #PUNKTACJA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.n == 2:
               if self.menu_position[self.n] == 1:
                   self.menu_position[self.n] = 0
               else:
                   self.menu_position[self.n] += 1
            #PIŁKA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.n == 2:
               if self.menu_position[self.n] == 3:
                   self.menu_position[self.n] = 0
               else:
                   self.menu_position[self.n] += 1
            #SIATKA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.n == 2:
               if self.menu_position[self.n] == 1:
                   self.menu_position[self.n] = 0
               else:
                   self.menu_position[self.n] += 1
            #SZEROKOSC I WYSOKOSC GRACZY
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.n == 3:
               if self.menu_position[self.n] == 2:
                   self.menu_position[self.n] = 0
               else:
                   self.menu_position[self.n] += 1
            #PREDKOSC SKOKU GRACZA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 1 and self.n == 3:
               if self.menu_position[self.n] == 2:
                   self.menu_position[self.n] = 0
               else:
                   self.menu_position[self.n] += 1
            #PREDKOSC PORUSZANIA SIE GRACZA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 2 and self.n == 3:
               if self.menu_position[self.n] == 2:
                   self.menu_position[self.n] = 0
               else:
                   self.menu_position[self.n] += 1
            #STALA GRAWITACJI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.n == 3:
               if self.menu_position[self.n] == 2:
                   self.menu_position[self.n] = 0
               else:
                   self.menu_position[self.n] += 1
            #SZYBKOSC CZASU
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.n == 3:
               if self.menu_position[self.n] == 3:
                   self.menu_position[self.n] = 0
               else:
                   self.menu_position[self.n] += 1
            #MAX DOZWOLONYCH ODBIC 
            elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 0 and self.n == 3:
               if self.menu_position[self.n] == 3:
                   self.menu_position[self.n] = 0
               else:
                   self.menu_position[self.n] += 1
            #ILOSC RUND
            elif self.menu_position[0] == 1 and self.menu_position[1] == 3 and self.menu_position[2] == 1 and self.n == 3:
               if self.menu_position[self.n] == 3:
                   self.menu_position[self.n] = 0
               else:
                   self.menu_position[self.n] += 1
            #PREDKOSC Y ODBICIA PILKI PRZEZ GRACZA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 0 and self.n == 3:
               if self.menu_position[self.n] == 3:
                   self.menu_position[self.n] = 0
               else:
                   self.menu_position[self.n] += 1
            #PREDKOSC Y ODBICIA PILKI OD SIATKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 1 and self.n == 3:
               if self.menu_position[self.n] == 3:
                   self.menu_position[self.n] = 0
               else:
                   self.menu_position[self.n] += 1
            #PREDKOSC X PILKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 2 and self.n == 3:
               if self.menu_position[self.n] == 3:
                   self.menu_position[self.n] = 0
               else:
                   self.menu_position[self.n] += 1
            #PROMIEN PILKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 4 and self.menu_position[2] == 3 and self.n == 3:
               if self.menu_position[self.n] == 3:
                   self.menu_position[self.n] = 0
               else:
                   self.menu_position[self.n] += 1
            #WYSOKOSC SIATKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 0 and self.n == 3:
               if self.menu_position[self.n] == 3:
                   self.menu_position[self.n] = 0
               else:
                   self.menu_position[self.n] += 1
            #SZEROKOSC SIATKI
            elif self.menu_position[0] == 1 and self.menu_position[1] == 5 and self.menu_position[2] == 1 and self.n == 3:
               if self.menu_position[self.n] == 3:
                   self.menu_position[self.n] = 0
               else:
                   self.menu_position[self.n] += 1
#ZAPIS WARTOSCI            
        if klawiatura[pygame.K_RETURN]:
            if self.menu_position[0] == 0:
                #WŁACZA SIE GRA
                self.menu_time = False
                pygame.mixer.music.stop
            elif self.menu_position[0] == 2 and self.n == 1:
                pass
            elif self.menu_position[0] == 3 and self.n == 1:
                pass

            #WIELKOSC OKNA
            elif self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.menu_position[2] == 0 and self.n == 2:
                self.zapis_do_pliku(4, 1280)
                self.zapis_do_pliku(5, 720)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.menu_position[2] == 1 and self.n == 2:
                self.zapis_do_pliku(4, 1366)
                self.zapis_do_pliku(5, 768)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.menu_position[2] == 2 and self.n == 2:
                self.zapis_do_pliku(4, 1920)
                self.zapis_do_pliku(5, 1080)
            
            #SZEROKOSC I WYSOKOSC GRACZY
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] == 0 and self.n == 3:
                self.zapis_do_pliku(1, 100)
                self.zapis_do_pliku(2, 50)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] == 1 and self.n == 3:
                self.zapis_do_pliku(1, 150)
                self.zapis_do_pliku(2, 75)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.menu_position[2] == 0 and self.menu_position[3] == 2 and self.n == 3:
                self.zapis_do_pliku(1, 200)
                self.zapis_do_pliku(2, 100)
            
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
                self.zapis_do_pliku(7, 12.0)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 0 and self.menu_position[3] == 2 and self.n == 3:
                self.zapis_do_pliku(7, 8.0)
            
            #SZYBKOSC CZASU
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] == 0 and self.n == 3:
                self.zapis_do_pliku(8, 0.2)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] == 1 and self.n == 3:
                self.zapis_do_pliku(8, 0.1)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] == 2 and self.n == 3:
                self.zapis_do_pliku(8, 0.5)
            elif self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.menu_position[2] == 1 and self.menu_position[3] == 3 and self.n == 3:
                self.zapis_do_pliku(8, 1.0)
            
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
                self.menu_position[self.n] = 0
                self.n -= 1

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
            data[numer_lini] = '%f\n' % (wartosc)
        #print(type(wartosc))
        #ZAPIS Z NOWYMI WARTOSCIAMI
        with open(path, 'w') as plik:
            plik.writelines(data)
        plik.close()

menu()