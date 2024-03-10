odpowiedzi = ["barcelona" , "real" , "city" , "goat" , "swinia" , "amator"]

def ramka(odpowiedzi):
    print("  _________________________")
    print(" |                         |")
    print(" | " + odpowiedzi[0] + " , " + odpowiedzi[1] + " , " + odpowiedzi[2] + " | ")
    print(" |_________________________|")

def ramka2(odpowiedzi):
    print("  _________________________")
    print(" |                         |")
    print(" | " + odpowiedzi[3] + " , " + odpowiedzi[4] + " , " + odpowiedzi[5] + "  | ")
    print(" |_________________________|")

def polecenie1():
    print("1. Odpowiedz na pytanie.")
    ramka(odpowiedzi)
    while True:
        odpowiedz = str(input("Kto wygra ucla? "))
        if odpowiedz == "barcelona":
            print("Jedyna dobra odpowiedz.")
            return True
        else:
            print("Bledna odpowiedz.")

def polecenie2():
    print("2. Uzupelnij zdanie.")
    ramka2(odpowiedzi)
    while True:
        odpowiedz1 = str(input("Messi to "))
        if odpowiedz1 == "goat":
            print("Jedyna dobra odpowiedz.")
            return True
        else:
            print("Bledna odpowiedz.")

print("Witaj w quizie")

zadaniedone = False
zadaniedone1 = False

while True:
    zadanie = int(input("Wybierz zadanie: 1 lub 2 "))
    if zadanie == 1:
        zadaniedone = polecenie1()
    elif zadanie == 2:
        zadaniedone1 = polecenie2()
    else:
        print("Nie ma takiego zadania.")
    
    if zadaniedone and zadaniedone1:
        print("Zrobiles wszystkie zadania.")
        break