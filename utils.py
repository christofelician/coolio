def widerstand20(laenge, querschnitt, leitwert):
    """Widerstand bei 20 Grad berechnen1"""
    wider20 = laenge / leitwert / querschnitt
    return wider20


def deltawiderstand(wide20, temperatur, temperaturkoeffizient):
    """Widerstand um wieviel der Widerstand im Vergleich zu R20 groeßer/kleiner wird"""
    deltawider = wide20 * (temperatur - 20) * temperaturkoeffizient
    return deltawider


def widerstand(wider20, deltar):
    """Widerstand bei angegebener Temperatur berechnen"""
    return wider20 + deltar


def absspannungsabfall(widerstan, strom):
    """Wabsoluter Spannungsabfall am Widerstand"""
    return widerstan * strom


def relspannungsabfall(spannung, abspannungsabfall):
    """Wrelativer Spannungsabfall am Widerstand"""
    return (spannung - abspannungsabfall) / spannung
