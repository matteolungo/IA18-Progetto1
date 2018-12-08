"""
    File name: main.py
    Author: Matteo Lungo
    Date created: 05/12/2018
    Date last modified: 08/12/2018
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
    exit()
elif not ((max - min) % b) == 0:
    print("max-min non è multiplo di b")
    exit()
else:
    s = Structure(min, max, b)
    s.arrayPrint()
    s.structPrint()

    """
    METODI:
    
    insert(key, value) - inserisce una coppia (chiave, valore)
    delete(key) - elimina una chiave e il valore associato
    search(key) - restituisce il valore assegnato alla chiave
    print() - mostra la struttura
    """


def insert(key, value):
    s.insert(key, value)


def delete(key):
    s.delete(key)


def search(key):
    s.search(key)


def print():
    s.structPrint()


def takeInput():
    exec(input())
    takeInput()


takeInput()
