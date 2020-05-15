import os

class settings(object):
    #USTAWIENIA:
    def __init__(self):
        #DZIAŁANIE GRY
        self.max_fps = 60.0
        self.foxygame = True
        #KOLORY
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (129, 187, 129)
        self.GRAY = (205, 205, 205)
        self.RED = (255, 0, 0)
        #ODCZYT Z PLIKU
        current_path = os.getcwd()
        path = current_path+'/settings/parameters.txt'
        with open(path, 'r') as plik:
            data = plik.readlines()
        #WIELKOSC GRACZY
        self.szerokosc_graczy = int(data[1])
        self.wysokosc_graczy = int(data[2])
        #WIELKOSC OKNA
        self.WIDTH = int(data[4])
        self.HEIGHT = int(data[5])
        #FIZYKA
        self.g = float(data[7])
        self.dt = float(data[8])
        #GRACZ
        self.wysokosc_skoku = int(data[10])
        self.szybkosc_poruszania = int(data[11])
        #PUNKTACJA
        self.max_dozwolonych_odbic = int(data[13])
        self.max_liczba_punktow = int(data[14])
        #PIŁKA
        self.wysokosc_odbicia_pilki_przez_gracza = int(data[16])
        self.wysokosc_odbicia_pilki_od_siatki = int(data[17])
        self.szybkosc_pilki_x = int(data[18])
        plik.close()