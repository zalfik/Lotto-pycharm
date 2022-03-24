import random

tablica, kupon = [], [7, 18, 22, 26, 33, 49]
trafienia, proby, kasa = 0, 0, 0


def wypelnienie (tab):
    while len(tab) < 6:
        x = random.randint(1, 49)
        if not tab.count(x):
            tab.append(x)


def sprawdzenie (tab, kpn, traf):
    for i in kpn:
        if tab.count(i):
            traf += 1
    return traf


while trafienia < 3:
    trafienia = 0
    tablica.clear()
    wypelnienie(tablica)
    tablica.sort()
    print(tablica)
    sprawdzenie(tablica, kupon, trafienia)
    trafienia = sprawdzenie(tablica, kupon, trafienia)
    print("Liczba trafień: ", trafienia)
    proby += 1
    kasa += 3
print("Liczba prób: ", proby)
print("Wydane pieniądze:", kasa, "zł")
