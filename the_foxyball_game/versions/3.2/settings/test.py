import os

#ODCZYT Z PLIKU
#szerokosc_gracza = 0
#wysokosc_gracza = 0
#current_path = os.getcwd()
#path = current_path+'/parameters.txt'
#print(path)
#plik = open(path, 'r')
#nr_lini = 0
#for linia in plik.readlines():
#    nr_lini += 1
#    print(linia[:-1])
#    if nr_lini == 2:
#        szerokosc_gracza = int(linia[:-1])
#    if nr_lini == 3:
#        wysokosc_gracza = int(linia[:-1])
#nr_lini = 0
#plik.close()
#print("szerokosc: %d | wysokosc: %d" % (szerokosc_gracza, wysokosc_gracza))

#ODCZYT Z PLIKU
szerokosc_gracza = 0
wysokosc_gracza = 0

current_path = os.getcwd()
path = current_path+'/parameters.txt'
#print(path)
with open(path, 'r') as plik:
    data = plik.readlines()
szerokosc_gracza = int(data[1])+50
wysokosc_gracza = int(data[2])+50
plik.close()
#print("szerokosc: %d | wysokosc: %d" % (szerokosc_gracza, wysokosc_gracza))

#ZAPIS DO PLIKU

#WARTOSCI KTORE CHCEMY ZAPISAC
#szerokosc_gracza = 100
#wysokosc_gracza = 50
#ZAPIS POPRZEDNIEGO STANU
current_path = os.getcwd()
path = current_path+'/parameters.txt'
#print(path)
with open(path, 'r') as plik:
    data = plik.readlines()
#NADPISANIE KONKRETNEJ LINI
data[1] = '%d\n' % (szerokosc_gracza)
data[2] = '%d\n' % (wysokosc_gracza)
#ZAPIS Z NOWYMI WARTOSCIAMI
with open(path, 'w') as plik:
    plik.writelines(data)
plik.close()
