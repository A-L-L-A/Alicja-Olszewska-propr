STOSUNEK_FAHRENHEITA_DO_CELSJUSZA = 9 / 5
PRZESUNIECIE_ZERA_FAHRENHEITA = 32


def celsjusz_na_fahrenheit(temperatura_celsjusza: float) -> float:
    return temperatura_celsjusza * STOSUNEK_FAHRENHEITA_DO_CELSJUSZA + PRZESUNIECIE_ZERA_FAHRENHEITA


def pobierz_temperature() -> float:
    return float(input("Podaj temperaturę w °C: "))


temperatura_c = pobierz_temperature()
temperatura_f = celsjusz_na_fahrenheit(temperatura_c)

print(f"{temperatura_c}°C to {temperatura_f:.1f}°F")