from random import randint

flag = True
moje_nieruchomości = []
kwoty = [0, 0, 100, 200, 0, 200, 300, 0, 300, 400, 0, 600]
dzialanie = ""
kupowanie = ""
x = ""
napis = ""
licznik_pozycji = 1
kostka = 0
kasa = 2000
licznik_kupienia = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
nieruchomosci = [" ", " ","Park Początkowy","Osiedle Przyjaźni", " ","Aleja Wolności","Fabryka Piękna", " ","Ulica Fabryczna","Aleja Rusa", " ","Park Nowogradzki"]
tablica = ["-", "-", "-", "-",
           "-", "-", "-", "-",
           "-", "-", "-", "-", "-"]
ruch = "X"
def narysowanatablica(tablica):
    print("     W ", "U.F", "A.R", " P")
    print("   | " + tablica[7] + " | " + tablica[8] + " | " + tablica[9] + " | " + tablica[10] + " | ")
    print("F.P| " + tablica[6] + " | ", "     | " + tablica[11] + " |P.N ")
    print("A.W| " + tablica[5] + " | ", "     | " + tablica[12] + " |K.P ")
    print("   | " + tablica[4] + " | " + tablica[3] + " | " + tablica[2] + " | " + tablica[1] + " | ")
    print("    W.O", "O.P", "P.P", "STR")
def wiezienie():
    global kasa
    kasa -= 200
    print("Wylosowałeś", kostka, "na kostce idziesz o tyle miejsc")
    print("Trafileś na Więzienie")
    print("Opłata 200zł")
def ulicafabryczna():
    print("Wylosowałeś", kostka, "na kostce idziesz o tyle miejsc")
    print("Trafileś na Ulice Fabryczną")

def aleja_rusa():
    print("Wylosowałeś", kostka, "na kostce idziesz o tyle miejsc")
    print("Trafileś na Aleje Rusa")

def parking():
    print("Wylosowałeś", kostka, "na kostce idziesz o tyle miejsc")
    print("Trafileś na Parking")

def parknowogradzki():
    print("Wylosowałeś", kostka, "na kostce idziesz o tyle miejsc")
    print("Trafileś na Park Nowogradzki")

def kontrolapredkosci():
    global kasa
    kasa -= 400
    print("Wylosowałeś", kostka, "na kostce idziesz o tyle miejsc")
    print("Trafileś na Kontrolę Prędkości")
    print("Opłata 400zł")
def start():
    print("Wylosowałeś", kostka, "na kostce idziesz o tyle miejsc")
    print("Trafileś na Start")
def parkpoczatkowy():
    print("Wylosowałeś", kostka, "na kostce idziesz o tyle miejsc")
    print("Trafileś na Park Początkowy")

def osiedleprzyjazni():
    print("Wylosowałeś", kostka, "na kostce idziesz o tyle miejsc")
    print("Trafileś na Osiedle Przyjaźni")

def wyplacanieodsetek():
    global kasa
    kasa += 500
    print("Wylosowałeś", kostka, "na kostce idziesz o tyle miejsc")
    print("Trafileś na Wypłacanie odsetek")
    print("+500zł dla gracza")
def alejawolnosci():
    print("Wylosowałeś", kostka, "na kostce idziesz o tyle miejsc")
    print("Trafileś na Aleje Wolności")

def fabrykapiekna():
    print("Wylosowałeś", kostka, "na kostce idziesz o tyle miejsc")
    print("Trafileś na Fabryke Piękna")

def choose(wybor):
    if wybor == "rzut":
        global licznik_pozycji
        global kostka
        kostka = randint(1, 4)
        licznik_pozycji += kostka
    elif wybor == "stan konta":
        print("Twój stan konta wynosi: ", kasa)
    elif wybor == "moje nieruchomości":
        if len(moje_nieruchomości) == 0:
            print("Nie posiadasz żadnych nieruchomości")
        else:
            for p in moje_nieruchomości:
                print(p)
    elif wybor == "brakuje":
        print("Twoje brakujące nieruchomości:")
        for l in nieruchomosci:
            if l != " ":
                print(l)

    elif wybor == "exit":
        print("Pomyślnie wyłączono")
        exit()
    else:
        global dzialanie
        dzialanie = "nic"

while kasa > 0 and len(moje_nieruchomości) != 7:

    if flag:
        tablica[1] = ruch
        flag = False
        narysowanatablica(tablica)
        tablica[1] = "-"

    dzialanie = input("Dostępne akcje>>>rzut/stan konta/moje nieruchomości/brakuje/exit: ")
    choose(dzialanie)
    if dzialanie == "nic":
        continue
    if dzialanie == "stan konta":
        continue
    if dzialanie == "moje nieruchomości":
        continue
    if dzialanie == "brakuje":
        continue

    for l in range(0,9):
        print()

    if licznik_pozycji > 12:
        licznik_pozycji -= 12
        kasa += 200
        print("+ 200zł za przejscie")

    if licznik_pozycji == 1:
        start()
    if licznik_pozycji == 2:
        parkpoczatkowy()
    if licznik_pozycji == 3:
        osiedleprzyjazni()
    if licznik_pozycji == 4:
        wyplacanieodsetek()
    if licznik_pozycji == 5:
        alejawolnosci()
    if licznik_pozycji == 6:
        fabrykapiekna()
    if licznik_pozycji == 7:
        wiezienie()
    if licznik_pozycji == 8:
        ulicafabryczna()
    if licznik_pozycji == 9:
        aleja_rusa()
    if licznik_pozycji == 10:
        parking()
    if licznik_pozycji == 11:
        parknowogradzki()
    if licznik_pozycji == 12:
        kontrolapredkosci()

    tablica[licznik_pozycji] = ruch
    print()
    narysowanatablica(tablica)
    if licznik_kupienia[licznik_pozycji] == 0:
        if licznik_pozycji == 2 or licznik_pozycji == 3 or licznik_pozycji == 5 or licznik_pozycji == 6 or licznik_pozycji == 8 or  licznik_pozycji == 9 or licznik_pozycji == 11:
            print("Koszt tego pola wynosi", kwoty[licznik_pozycji], "zł")

            while True:
                if kasa > kwoty[licznik_pozycji]:
                    kasa -= kwoty[licznik_pozycji]
                else:
                    print("Nie stać cie na zakup")
                    break
                kupowanie = input("Czy chcesz kupic>>>tak/nie: ")
                if kupowanie == "tak":
                    moje_nieruchomości.append(nieruchomosci[licznik_pozycji])
                    nieruchomosci[licznik_pozycji]= " "
                    print("Zakupiono")
                    licznik_kupienia[licznik_pozycji] += 1
                    break
                if kupowanie == "nie":
                    print("Nie zakupiono")
                    break
    else:
        print("Ta nieruchomość jest juz przez ciebie zakupiona")
    tablica[licznik_pozycji] = "-"
if kasa <= 0:
    print("Nie masz kasy przegrałeś grę")
if len(moje_nieruchomości) == 7:
    print("Kupiłeś wszystkie nieruchomości wygrałeś grę")

