from Structure import *
from timeit import default_timer
from random import randint
import sys, os


def blockPrint():
    sys.stdout = open(os.devnull, 'w')


def enablePrint():
    sys.stdout = sys.__stdout__


def structurePerformance(min, max, struct):
    start = default_timer()
    for i in range(min, max):
        struct.insert(randint(1, 1000000), i)
    elapsed = default_timer() - start
    print(f"Tempo totale per {max - min} operazioni di INSERT: {elapsed} s")
    print("Tempo medio INSERT:", elapsed / (max - min), " s")

    start = default_timer()
    for i in range(min, max):
        blockPrint()
        struct.search(randint(1, 1000000))
        enablePrint()
    elapsed = default_timer() - start
    print(f"Tempo totale per {max - min} operazioni di SEARCH: {elapsed} s")
    print("Tempo medio SEARCH:", elapsed / (max - min), " s")

    start = default_timer()
    for i in range(min, max):
        struct.delete(randint(1, 1000000))
    elapsed = default_timer() - start
    print(f"Tempo totale per {max - min} operazioni di DELETE: {elapsed} s")
    print("Tempo medio DELETE:", elapsed / (max - min), " s")


def dictPerformance(ops, dic):
    start = default_timer()
    for i in range(ops):
        dic.update({i: i + 10})
    elapsed = default_timer() - start
    print(f"Tempo totale per {ops} operazioni di INSERT: {elapsed} s")
    print("Tempo medio INSERT:", elapsed / ops, " s")

    start = default_timer()
    for i in reversed(range(ops)):
        dic.get(i)
    elapsed = default_timer() - start
    print(f"Tempo totale per {ops} operazioni di SEARCH: {elapsed} s")
    print("Tempo medio SEARCH:", elapsed / ops, " s")

    start = default_timer()
    for i in range(ops):
        dic.pop(i)
    elapsed = default_timer() - start
    print(f"Tempo totale per {ops} operazioni di DELETE: {elapsed} s")
    print("Tempo medio DELETE:", elapsed / ops, " s")

if __name__ == "__main__":
    print("-- 100 elementi --")
    print("STRUCTURE")
    min = 0
    max = 100
    b = 50
    v = Structure(min, max, b)
    structurePerformance(min, max, v)
    print("DICTIONARY")
    dic = {}
    dictPerformance(100, dic)

    print("-- 1000 elementi --")
    print("STRUCTURE")
    min = 0
    max = 1000
    b = 500
    v = Structure(min, max, b)
    structurePerformance(min, max, v)
    print("DICTIONARY")
    dic = {}
    dictPerformance(1000, dic)

    print("-- 10000 elementi --")
    print("STRUCTURE")
    min = 0
    max = 10000
    b = 5000
    v = Structure(min, max, b)
    structurePerformance(min, max, v)
    print("DICTIONARY")
    dic = {}
    dictPerformance(10000, dic)

    print("-- 100000 elementi --")
    print("STRUCTURE")
    min = 0
    max = 100000
    b = 50000
    v = Structure(min, max, b)
    structurePerformance(min, max, v)
    print("DICTIONARY")
    dic = {}
    dictPerformance(100000, dic)

    print("-- 1000000 elementi --")
    print("STRUCTURE")
    min = 0
    max = 1000000
    b = 500000
    v = Structure(min, max, b)
    structurePerformance(min, max, v)
    print("DICTIONARY")
    dic = {}
    dictPerformance(1000000, dic)
