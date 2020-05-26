import os, pygame

class settings(object):
    #USTAWIENIA:
    def __init__(self):
        pygame.init()
        #DZIAŁANIE GRY
        self.max_fps = 60.0
        self.foxygame = True
        #KOLORY
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (129, 187, 129)
        self.GRAY = (205, 205, 205)
        self.RED = (255, 0, 0)
        self.ORANGE = (255,165,0)
        #ODCZYT Z PLIKU
        current_path = os.getcwd()
        path = current_path+'/settings/parameters.txt'
        with open(path, 'r') as plik:
            data = plik.readlines()
        #WIELKOSC OKNA
        self.WIDTH = int(data[4])
        self.HEIGHT = int(data[5])
        #MNOZNIK
        self.mnoznik_obiektow = self.WIDTH/1280
        #WIELKOSC GRACZY
        self.szerokosc_graczy = int(self.mnoznik_obiektow*int(data[1]))
        self.wysokosc_graczy = int(self.mnoznik_obiektow*int(data[2]))
        #FIZYKA
        self.g = float(self.mnoznik_obiektow*float(data[7]))
        self.dt = float(data[8])
        #GRACZ
        self.wysokosc_skoku = float(self.mnoznik_obiektow*int(data[10]))
        self.szybkosc_poruszania = float(self.mnoznik_obiektow*int(data[11]))
        #PUNKTACJA
        self.max_dozwolonych_odbic = int(data[13])
        self.max_liczba_punktow = int(data[14])
        #PIŁKA
        self.wysokosc_odbicia_pilki_przez_gracza = float(self.mnoznik_obiektow*int(data[16]))
        self.wysokosc_odbicia_pilki_od_siatki = float(self.mnoznik_obiektow*int(data[17]))
        self.szybkosc_pilki_x = float(self.mnoznik_obiektow*int(data[18]))
        self.promien_pilki = int(self.mnoznik_obiektow*int(data[19]))
        #SIATKA
        self.wysokosc_siatki = int(self.mnoznik_obiektow*int(data[21]))
        self.szerokosc_siatki = int(self.mnoznik_obiektow*int(data[22]))
        plik.close()
        #CZCIONKA
        self.font_72 = pygame.font.Font('fonts/ostrich-regular.ttf', int(self.mnoznik_obiektow*78))
        self.font_72_heavy = pygame.font.Font('fonts/ostrich-heavy.otf', int(self.mnoznik_obiektow*78))
        self.font_42 = pygame.font.Font('fonts/ostrich-regular.ttf', int(self.mnoznik_obiektow*42))
        self.font_42_heavy = pygame.font.Font('fonts/ostrich-heavy.otf', int(self.mnoznik_obiektow*42))
        self.font_56 = pygame.font.Font('fonts/ostrich-regular.ttf', int(self.mnoznik_obiektow*56))
        self.font_28 = pygame.font.Font('fonts/ostrich-regular.ttf', int(self.mnoznik_obiektow*28))