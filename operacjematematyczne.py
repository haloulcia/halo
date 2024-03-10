from random import randint

losliczba = randint(1,20)
wybor = 0
licznik = 0
while wybor != losliczba:
    licznik += 1
    wybor = int(input("Podaj liczbe z przedzialu 1-20: "))
    if wybor < 1 or wybor > 20:
        print("Podales liczbe nie znajdujaca sie w przedziale")
    if wybor == losliczba:
        break
    if wybor > losliczba:
        print("Twoja liczba jest mniejsza od podanej")
    else:
        print("Twoja liczba jest wieksza od podanej")
print("Udalo ci się odgadnąć liczbę")
print("Zajeło ci to: ", licznik, " prób")
