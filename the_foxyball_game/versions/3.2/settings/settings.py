class settings(object):
    #USTAWIENIA:
    def __init__(self):
        #WIELKOSC GRACZY
        self.szerokosc_graczy = 100
        self.wysokosc_graczy = 50
        #WIELKOSC OKNA
        self.WIDTH = 1280
        self.HEIGHT = 720
        #KOLORY
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (129, 187, 129)
        self.GRAY = (205, 205, 205)
        self.RED = (255, 0, 0)
        #USTAWIENIA GRY
        self.g = 9.81
        self.dt = 0.2
        self.max_fps = 60.0