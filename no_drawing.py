import pygame

# Nastavitve za pygame
pygame.init()
sirina, visina = 1200, 800
win = pygame.display.set_mode((sirina, visina))
pygame.display.set_caption("Vizualizacija A* algoritma")

# Barve za pygame
bela = (255, 255, 255)
crna = (0, 0, 0) # 1
siva = (128, 128, 128)
rdeca = (255, 0, 0) # 9
zelena = (0, 255, 0) # 8
vijolicna = (128, 0, 128) # 4
oranzna = (255, 165, 0) # 2
turkizna = (64, 224, 208) # 3

velikost_polj = 10
vrstice = visina // velikost_polj
stolpci = sirina // velikost_polj

mapa = [[0 for x in range(stolpci)] for y in range(vrstice)]

def narisi_mapo():
    win.fill(bela)
    for vrsta in range(vrstice):
        for stolpec in range(stolpci):
            x = stolpec * velikost_polj
            y = vrsta * velikost_polj
            pygame.draw.rect(win, siva, (x, y, velikost_polj, velikost_polj), 1)

            if mapa[vrsta][stolpec] == 1:
                pygame.draw.rect(win, crna, (x, y, velikost_polj, velikost_polj))
            
            if mapa[vrsta][stolpec] == 8:
                pygame.draw.rect(win, zelena, (x, y, velikost_polj, velikost_polj))
            
            if mapa[vrsta][stolpec] == 9:
                pygame.draw.rect(win, rdeca, (x, y, velikost_polj, velikost_polj))

            if mapa[vrsta][stolpec] == 2:
                pygame.draw.rect(win, oranzna, (x, y, velikost_polj, velikost_polj))
            
            if mapa[vrsta][stolpec] == 3:
                pygame.draw.rect(win, turkizna, (x, y, velikost_polj, velikost_polj))

            if mapa[vrsta][stolpec] == 4:
                pygame.draw.rect(win, vijolicna, (x, y, velikost_polj, velikost_polj))

    pygame.display.update()

def polozaj_klika(polozaj):
    x, y = polozaj
    stolpec = x // velikost_polj
    vrsta = y // velikost_polj
    return stolpec, vrsta

class Polje(): # Objekt Polje
    def __init__(self, pozicija, g = 0, h = 0, prejšnji = None):
        self.pozicija = pozicija
        self.g_cena = g
        self.h_cena = h
        self.f_cena = self.g_cena + self.h_cena
        self.prejsnji = prejšnji

def razdalja(polje, cilj): # Razdalja med poljem in nekim drugim poljem (vnesemo KOORDINATE, ne objekta)
    razdalja_x = abs(polje[0] - cilj[0])
    razdalja_y = abs(polje[1] - cilj[1])
    return 100 * (razdalja_x + razdalja_y) + (141 - 2 * 100) * min(razdalja_x, razdalja_y)

def algoritem(mapa, zacetek, konec): # Algoritem A*
    nepregledana = [] # Vsa polja, na katerih še nismo stali
    pregledana = [] # Vsa polja, na katerih smo že stali

    razdalja_x = abs(zacetek[0] - konec[0])
    razdalja_y = abs(zacetek[0] - konec[0])

    # Ustvarimo začetek in konec
    zacetek = Polje(zacetek, g = 0, h = 100 * (razdalja_x + razdalja_y) + (141 - 2 * 100) * min(razdalja_x, razdalja_y))
    konec = Polje(konec, h = 0)
    nepregledana.append(zacetek)

    trenutno = nepregledana[0]

    while trenutno.pozicija != konec.pozicija:
        maketa = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)] # Polja, sosednja trenutnemu polju
        sosedi = [(trenutno.pozicija[0] + x, trenutno.pozicija[1] + y) for x, y in maketa]

        # n_pos = [polje.pozicija for polje in nepregledana]
        # print(n_pos)
        # print(len(nepregledana), trenutno.pozicija)
        # print(sosedi)
        # print("--------------------------------")

        for sosed in sosedi:

            if sosed[0] > (len(mapa[0]) - 1) or sosed[1] > (len(mapa) - 1) or sosed[0] < 0 or sosed[1] < 0: # Preverimo, če je polje v mreži
                continue

            if mapa[sosed[1]][sosed[0]] == 2 or mapa[sosed[1]][sosed[0]] == 8:
                continue
            
            if mapa[sosed[1]][sosed[0]] == 1: # Preverimo, če je polje ovira
                continue
            
            if abs(sosed[0] - trenutno.pozicija[0]) == 1 and abs(sosed[1] - trenutno.pozicija[1]) == 1: # Izračunamo razdaljo polja do 'trenutnega' polja
                razdalja_prejsnji = 141
            else:
                razdalja_prejsnji = 100

            preskoci = False
            for polje in nepregledana: 
                if sosed == polje.pozicija: # Pogledamo, če smo polje že ustvarili in če je pot do njega cenejša
                    if polje.g_cena > trenutno.g_cena + razdalja_prejsnji:
                        polje.g_cena = trenutno.g_cena + razdalja_prejsnji
                        polje.f_cena = polje.g_cena + polje.h_cena
                        polje.prejsnji = trenutno
                    preskoci = True
                    break

            if preskoci == True:
                continue
            
            # Če ne drži nobeden od prejšnjih pogojev, polje še ni bilo ustvarjeno
            novo_polje = Polje(sosed, trenutno.g_cena + razdalja_prejsnji, razdalja(sosed, konec.pozicija), trenutno)
            nepregledana.append(novo_polje)
            if novo_polje.pozicija != zacetek.pozicija and novo_polje.pozicija != konec.pozicija:
                mapa[novo_polje.pozicija[1]][novo_polje.pozicija[0]] = 3
                # narisi_mapo()
        
        nepregledana.remove(trenutno) # Odstranimo trenutno polje s seznama nepregledanih polj
        pregledana.append(trenutno) # Polje prestavmo k pregledanim poljem
        if trenutno.pozicija != zacetek.pozicija and trenutno.pozicija != konec.pozicija:
            mapa[trenutno.pozicija[1]][trenutno.pozicija[0]] = 2
            # narisi_mapo()

        najmanjsi_f = 2147483647
        polja = []
        h = []
        for polje in nepregledana:
            if polje.f_cena < najmanjsi_f:
                h.clear()
                polja.clear()               
                najmanjsi_f = polje.f_cena
                h.append(polje.h_cena)
                polja.append(polje)
            elif polje.f_cena == najmanjsi_f:
                h.append(polje.h_cena)
                polja.append(polje)
        
        trenutno = polja[h.index(min(h))]

    pot = []
    while trenutno.prejsnji != None:
        if trenutno.pozicija != zacetek.pozicija and trenutno.pozicija != konec.pozicija:
            mapa[trenutno.pozicija[1]][trenutno.pozicija[0]] = 4
            # narisi_mapo()
        pot.append(trenutno.pozicija)
        trenutno = trenutno.prejsnji
    
    pot.append(zacetek.pozicija)
        
def main():
    poteka = True # Program poteka
    risemo = False # Drzimo dol misko
    zacetek = None # Zacetno polje
    konec = None # Koncno polje
    racuna = False # Algoritem je zacel

    while poteka == True:
        for dogodek in pygame.event.get():
            if dogodek.type == pygame.QUIT: # Če pritisnemo 'X'
                poteka = False
            
            elif dogodek.type == pygame.MOUSEBUTTONDOWN: # Če kliknemo
                if dogodek.button == 1:  
                    pozicija_klik = pygame.mouse.get_pos()
                    stolpec_klik, vrstica_klik = polozaj_klika(pozicija_klik)
                    if zacetek == None:
                        zacetek = (stolpec_klik, vrstica_klik)
                        mapa[vrstica_klik][stolpec_klik] = 8
                    elif konec == None:
                        konec = (stolpec_klik, vrstica_klik)
                        mapa[vrstica_klik][stolpec_klik] = 9
                    elif (stolpec_klik, vrstica_klik) != zacetek and (stolpec_klik, vrstica_klik) != konec:
                        risemo = True
                        mapa[vrstica_klik][stolpec_klik] = 1 - mapa[vrstica_klik][stolpec_klik]

            elif dogodek.type == pygame.MOUSEBUTTONUP: # Če spustimo klik
                if dogodek.button == 1:  
                    risemo = False

            elif dogodek.type == pygame.MOUSEMOTION: # Če povlečemo miško med klikanjem
                if risemo == True:
                    pozicija_miska = pygame.mouse.get_pos()
                    stolpec_miska, vrstica_miska = polozaj_klika(pozicija_miska)
                    if (stolpec_miska, vrstica_miska) != zacetek and (stolpec_miska, vrstica_miska) != konec:
                        if mapa[vrstica_miska][stolpec_miska] != 1:
                            mapa[vrstica_miska][stolpec_miska] = 1
            
            if dogodek.type == pygame.KEYDOWN:
                if dogodek.key == pygame.K_SPACE and racuna == False:
                    try:
                        algoritem(mapa, zacetek, konec)
                    except:
                        print("Pot je nemogoče poiskati")
                        poteka = False
        
        narisi_mapo()
        pygame.display.update()
    
    pygame.quit()

# Zaženemo glavno funkcijo 
main()