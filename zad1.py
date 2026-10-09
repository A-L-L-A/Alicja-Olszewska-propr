from abc import ABC, abstractmethod
import math


class Figura(ABC):
    @abstractmethod
    def oblicz_pole(self):
        pass


class Kwadrat(Figura):
    def __init__(self, bok):
        self.bok = bok
    def oblicz_pole(self):
        return self.bok ** 2


class Prostokat(Figura):
    def __init__(self, szerokosc, wysokosc):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
    def oblicz_pole(self):
        return self.szerokosc * self.wysokosc


class Kolo(Figura):
    def __init__(self, promien):
        self.promien = promien

    def oblicz_pole(self):
        return math.pi * self.promien ** 2

figury = [
    Kwadrat(5),
    Prostokat(7, 8),
    Kolo(4)
]

for figura in figury:
    print(f"{figura.__class__.__name__}: {figura.oblicz_pole():.2f}")