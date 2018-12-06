"""
    File name: array.py
    Author: Matteo Lungo
    Date created: 05/12/2018
    Date last modified: 14/12/2018
    Python Version: 3.6

    Questo modulo contiene l'implementazione
    di un array che gestisce coppie di tipo (key, value)
"""

from dictTrees.avlTree import *
from dictionaries.linkedListDictionary import *


class Structure():

    def __init__(self, min, max, b):
        self.array = []
        self.structList = []
        self.min = min
        self.max = max
        self.r = 6
        self.b = b
        self.d = int(abs((self.max - self.min) / b))
        d = self.d
        n = 0
        for i in range(0, d + 2):
            self.array.append(n)
            self.structList.append(LinkedListDictionary())
            n = n + 1

    def arrayPrint(self):
        print(self.array, "\n")

    def structPrint(self):
        for i in range(0, len(self.array)):
            self.structList[i].print()
        print("\n")

    def insert(self, key, value):
        struct = self.structList
        i = self.index(key)
        struct[i].insert(key, value)
        self.control(struct[i])

    def delete(self, key):
        struct = self.structList
        i = self.index(key)
        struct[i].delete(key)
        self.control(struct[i])

    def search(self, key):
        struct = self.structList
        index = self.index(key)
        print(struct[index].search(key))

    def index(self, key):
        d = self.d
        b = self.b

        if key < self.min:
            print("Key below min.")
            exit()
        elif key > self.max:
            print("Key above max.")
            exit()
        for i in range(0, 7):
            if key >= ((self.min) + (i * b)) and key < ((self.min) + (i + 1) * b):
                return i

    def control(self, struct):
        if type(struct) == LinkedListDictionary and struct.lenght()>6:
            return self.listToAVL(struct)
        elif type(struct) == AVLTree and struct.lenght()<6:
            return self.AVLToList(struct)

    def listToAVL(self,struct):


    def AVLToList(self,struct):


if __name__ == "__main__":
    v = Structure(5, 40, 7)
    v.arrayPrint()
    v.insert(15, 30)
    v.insert(16, 32)
    v.insert(20, 40)
    v.structPrint()
    v.delete(15)
    v.structPrint()
    v.search(20)

