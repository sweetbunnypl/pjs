import pygame, sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (129, 187, 129)
GRAY = (205, 205, 205)
RED = (255, 0, 0)

WIDTH = 1280
HEIGHT = 720

pygame.init()
#music = pygame.mixer.music.load('../music/background_music.mp3')
#pygame.mixer.music.play(-1)
#font = pygame.font.Font('../fonts/ostrich-regular.ttf', 32)
font = pygame.font.Font('fonts/ostrich-regular.ttf', 32)

class menu(object):

    def __init__(self):
        self.max_fps = 60.0
        self.n = 0
        self.menu_position = [0,0,0,0]

        #SCREEN
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('The Foxyball Game')
        #self.background = pygame.transform.scale(pygame.image.load('../textures/background.png'), (WIDTH, HEIGHT))
        self.background = pygame.transform.scale(pygame.image.load('textures/background.png'), (WIDTH, HEIGHT))

        #PĘTLA
        self.clock = pygame.time.Clock()
        self.czas = 0.0
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

                #MAIN MENU
                if self.menu_position[0] == 0 and self.n == 0:
                    text = font.render("GRAJ", True, WHITE, GREEN)
                elif self.menu_position[0] != 0 and self.n == 0:
                    text = font.render("GRAJ", True, WHITE, BLACK)
                
                if self.menu_position[0] == 1 and self.n == 0:
                    text2 = font.render("USTAWIENIA", True, WHITE, GREEN)
                elif self.menu_position[0] != 1 and self.n == 0:
                    text2 = font.render("USTAWIENIA", True, WHITE, BLACK)
                
                if self.menu_position[0] == 2 and self.n == 0:
                    text3 = font.render("STEROWANIE", True, WHITE, GREEN)
                elif self.menu_position[0] != 2 and self.n == 0:
                    text3 = font.render("STEROWANIE", True, WHITE, BLACK)
                
                if self.menu_position[0] == 3 and self.n == 0:
                    text4 = font.render("AUTOR", True, WHITE, GREEN)
                elif self.menu_position[0] != 3 and self.n == 0:
                    text4 = font.render("AUTOR", True, WHITE, BLACK)

                if self.menu_position[self.n] == 4:
                    text5 = font.render("numeracja menu: (%d, %d, %d, %d) n: %d" % (self.menu_position[0], self.menu_position[1], self.menu_position[2], self.menu_position[3], self.n), True, WHITE, GREEN)
                elif self.menu_position[self.n] != 4:
                    text5 = font.render("numeracja menu: (%d, %d, %d, %d) n: %d" % (self.menu_position[0], self.menu_position[1], self.menu_position[2], self.menu_position[3], self.n), True, WHITE, BLACK)
                #SUB MENU USTAWIENIA
                if self.menu_position[0] == 1 and self.menu_position[1] == 0 and self.n == 1:
                    text = font.render("ROZMIAR GRACZY", True, WHITE, GREEN)
                elif self.menu_position[0] == 1 and self.menu_position[1] != 0 and self.n == 1:
                    text = font.render("ROZMIAR GRACZY", True, WHITE, BLACK)

                if self.menu_position[0] == 1 and self.menu_position[1] == 1 and self.n == 1:
                    text2 = font.render("WIELKOSC OKNA", True, WHITE, GREEN)
                elif self.menu_position[0] == 1 and self.menu_position[1] != 1 and self.n == 1:
                    text2 = font.render("WIELKOSC OKNA", True, WHITE, BLACK)

                if self.menu_position[0] == 1 and self.menu_position[1] == 2 and self.n == 1:
                    text3 = font.render("FIZYKA", True, WHITE, GREEN)
                elif self.menu_position[0] == 1 and self.menu_position[1] != 2 and self.n == 1:
                    text3 = font.render("FIZYKA", True, WHITE, BLACK)

                textRect = text.get_rect()
                textRect.center = (WIDTH/2, HEIGHT/10)
                textRect2 = text2.get_rect()
                textRect2.center = (WIDTH/2, HEIGHT/6)
                textRect3 = text3.get_rect()
                textRect3.center = (WIDTH/2, HEIGHT/4)
                textRect4 = text4.get_rect()
                textRect4.center = (WIDTH/2, HEIGHT/2)
                textRect5 = text4.get_rect()
                textRect5.center = (WIDTH/2, HEIGHT/1.5)

                self.screen.blit(text, textRect)
                self.screen.blit(text2, textRect2)
                self.screen.blit(text3, textRect3)
                self.screen.blit(text4, textRect4)
                self.screen.blit(text5, textRect5)
                pygame.display.flip()

    def odczyt_klawiszy(self):
        klawiatura = pygame.key.get_pressed()
        if klawiatura[pygame.K_LEFT] or klawiatura[pygame.K_a] or klawiatura[pygame.K_j]:
            pass
        if klawiatura[pygame.K_RIGHT] or klawiatura[pygame.K_d] or klawiatura[pygame.K_l]:
            pass
        if klawiatura[pygame.K_UP] or klawiatura[pygame.K_w] or klawiatura[pygame.K_i]:
            if self.menu_position[self.n] == 0:
                self.menu_position[self.n] = 3
            else:
                self.menu_position[self.n] -= 1
        if klawiatura[pygame.K_DOWN] or klawiatura[pygame.K_s] or klawiatura[pygame.K_k]:
            if self.menu_position[self.n] == 3:
                self.menu_position[self.n] = 0
            else:
                self.menu_position[self.n] += 1
        if klawiatura[pygame.K_RETURN]:
            if self.menu_position[0] == 0:
                #WŁACZA SIE GRA
                self.menu_time = False
            elif self.n == 3:
                pass
            else:
                self.n += 1
        if klawiatura[pygame.K_q]:
            if self.n == 0:
                pass
            else:
                self.menu_position[self.n] = 0
                self.n -= 1


menu()