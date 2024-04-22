from utils import widerstand20
from utils import deltawiderstand
from utils import widerstand
from utils import absspannungsabfall
from utils import relspannungsabfall


def main():
    """Hauptprogramm"""
    laenge = float(input("Laenge des Leiters: "))
    querschnitt = float(input("Querschnitt des Leiters in Quadratmillimeter: "))
    leitwert = float(input("Leitwert des Leiters in Millisiemens pro Meter: "))
    temperatur = float(input("Temperatur des Leiters in Grad Celsius: "))
    strom = float(input("Strom durch den Leiter in Ampere: "))
    spannung = float(input("angelegte Spannung in Volt: "))
    temperaturkoeffizient = float(input("Temperaturkoeffizienten des Materials: "))

    # Widerstand bei 20 Grad berechnen
    widerstand_20 = widerstand20(laenge, querschnitt, leitwert)

    # Delta-Widerstand berechnen
    delta_widerstand = deltawiderstand(widerstand_20, temperatur, temperaturkoeffizient)

    # Gesamtwiderstand bei angegebener Temperatur berechnen
    gesamtwiderstand = widerstand(widerstand_20, delta_widerstand)

    # Absoluten Spannungsabfall berechnen
    absoluter_spannungsabfall = absspannungsabfall(gesamtwiderstand, strom)

    # Relativen Spannungsabfall berechnen
    relativer_spannungsabfall = relspannungsabfall(spannung, absoluter_spannungsabfall)

    # Ergebnisse ausgeben
    print("Widerstand bei 20 Grad Celsius:", widerstand_20, "Ohm")
    print("Delta-Widerstand bei", temperatur, "Grad Celsius:", delta_widerstand, "Ohm")
    print("Gesamtwiderstand bei", temperatur, "Grad Celsius:", gesamtwiderstand, "Ohm")
    print("Absoluter Spannungsabfall:", absoluter_spannungsabfall, "Volt")
    print("Relativer Spannungsabfall:", relativer_spannungsabfall)


if __name__ == "__main__":
    main()
