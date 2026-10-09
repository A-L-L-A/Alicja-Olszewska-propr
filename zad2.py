from enum import Enum


class TypTransportu(Enum):
    AUTOBUS = 1.5   # cena za km
    POCIAG = 3
    SAMOLOT = 10


def oblicz_cene_biletu(typ: TypTransportu, kilometry: float) -> float:
    return kilometry * typ.value


def wybierz_transport() -> TypTransportu:
    print("Wybierz typ transportu:")
    for numer, typ in enumerate(TypTransportu, start=1):
        print(f"{numer}. {typ.name.lower()}")

    wybor = int(input("Podaj numer: "))
    return list(TypTransportu)[wybor - 1]


transport = wybierz_transport()
kilometry = float(input("Ile kilometrów jedziesz: "))

print(f"Cena biletu: {oblicz_cene_biletu(transport, kilometry):.2f} zł")