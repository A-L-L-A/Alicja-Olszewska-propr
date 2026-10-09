from enum import Enum
class Operacja(Enum):
    DODAWANIE = "dodaj"
    ODEJMOWANIE = "odejmij"
    MNOZENIE = "mnoz"
    DZIELENIE = "dzielenie"

    
class Dzielenie(Exception):
    pass
def oblicz(a: float, b: float, operacja: Operacja) -> float:
    wynik = None
    match operacja:
        case Operacja.DODAWANIE:
            wynik = a + b
        case Operacja.ODEJMOWANIE:
            wynik = a - b
        case Operacja.MNOZENIE:
            wynik = a * b
        case operacja.DZIELENIE:
            if b != 0:
                wynik = a / b
            else:
                raise Dzielenie('Przez 0 sie nie dzieli')
    return wynik