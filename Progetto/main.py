"""
    File name: main.py
    Author: Matteo Lungo
    Date created: 05/12/2018
    Date last modified: 07/12/2018
    Python Version: 3.6

    Questo modulo contiene l'inizializzazione e
    le istruzioni di utilizzo della struttura Structure.

"""

from Structure import *

min = int(input("Inserire min: \n"))
max = int(input("Inserire max: \n"))
b = int(input("Inserire b: \n"))

if not b > 6:
    print("b non è maggiore di 6")
elif not ((max - min) % b) == 0:
    print("max-min non è multiplo di b")
else:
    s = Structure(min, max, b)
    print("Struttura:\n")
    s.structPrint()

    """
    METODI:
    
    insert(key, value) - inserisce una coppia (chiave, valore)
    delete(key) - elimina una chiave e il valore associato
    search(key) - restituisce il valore assegnato alla chiave
    """

if __name__ == "__main__":
    v = Structure(5, 40, 7)
    v.arrayPrint()

    v.insert(10, 20)
    v.insert(20, 40)
    v.insert(25, 50)
    v.insert(30, 60)
    v.insert(50, 100)

    v.structPrint()

    v.insert(11, 22)
    v.insert(12, 24)
    v.insert(13, 26)
    v.insert(14, 28)
    v.insert(15, 30)
    v.insert(16, 32)
    v.structPrint()

    v.insert(17, 34)
    v.structPrint()

    v.delete(17)
    v.structPrint()

    v.search(10)
    v.search(20)

    v.insert(60, 120)