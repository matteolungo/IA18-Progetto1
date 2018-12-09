from Structure import *
from time import time
import sys, os

def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__

def structurePerformance(min, max, struct):
    start = time()
    for i in range(min, max):
        struct.insert(i, i * 2)
    elapsed = time() - start
    print(f"Tempo totale per {max - min} operazioni di INSERT: {elapsed} s")
    print("Tempo medio INSERT:", elapsed / (max - min), " s")

    start = time()
    for i in range(min, max):
        blockPrint()
        struct.search(i)
        enablePrint()
    elapsed = time() - start
    print(f"Tempo totale per {max - min} operazioni di SEARCH: {elapsed} s")
    print("Tempo medio SEARCH:", elapsed / (max - min), " s")

    start = time()
    for i in range(min, max):
        struct.delete(i)
    elapsed = time() - start
    print(f"Tempo totale per {max - min} operazioni di DELETE: {elapsed} s")
    print("Tempo medio DELETE:", elapsed / (max - min), " s")


if __name__ == "__main__":
    print("-- 100 elementi --")
    min = 0
    max = 100
    b = 10
    v = Structure(min, max, b)
    structurePerformance(min, max, v)

    print("-- 1000 elementi --")
    min = 0
    max = 1000
    b = 100
    v = Structure(min, max, b)
    structurePerformance(min, max, v)

    print("-- 10000 elementi --")
    min = 0
    max = 10000
    b = 1000
    v = Structure(min, max, b)
    structurePerformance(min, max, v)
