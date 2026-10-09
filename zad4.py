from enum import Enum


class RodzajPojazdu(Enum):
    MOTOCYKL = 1500  # bazowa składka w zł
    SAMOCHOD = 1000
    CIEZAROWKA = 2000


def wspolczynnik_wieku(wiek):
    if wiek < 25:
        return 1.5
    if wiek < 65:
        return 1.0
    return 1.3


def oblicz_skladke(pojazd, wiek, liczba_szkod):
    wspolczynnik_szkod = 1 + liczba_szkod * 0.2
    return pojazd.value * wspolczynnik_wieku(wiek) * wspolczynnik_szkod


nazwa = input("Rodzaj pojazdu (motocykl, samochod, ciezarowka): ")
pojazd = RodzajPojazdu[nazwa.upper()]
wiek = int(input("Ile masz lat: "))
liczba_szkod = int(input("Ile szkód miałeś: "))

print("Składka:", round(oblicz_skladke(pojazd, wiek, liczba_szkod), 2), "zł")