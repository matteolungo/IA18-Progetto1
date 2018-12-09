"""
    File name: Structure.py
    Author: Matteo Lungo
    Date created: 05/12/2018
    Date last modified: 08/12/2018
    Python Version: 3.6

    Questo modulo contiene l'implementazione
    di una struttura dati che gestisce coppie di tipo (key, value)
    mediante liste concatenate  ed alberi AVL

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
        n = 0
        if not b > 6:
            print("b non è maggiore di 6")
            exit()
        elif not ((max - min) % b) == 0:
            print("max-min non è multiplo di b")
            exit()
        else:
            for i in range(0, self.d + 2):
                self.array.append(n)
                self.structList.append(LinkedListDictionary())
                n = n + 1

    def arrayPrint(self):
        print("Array:", self.array, "\n")

    def structPrint(self):
        print("Struttura:\n")
        for i in range(0, len(self.array)):
            print(i)
            self.structList[i].print()
        print("\n")

    def insert(self, key, value):
        structList = self.structList
        i = self.index(key)
        structList[i].insert(key, value)
        self.control(structList[i], i)

    def delete(self, key):
        structList = self.structList
        i = self.index(key)
        structList[i].delete(key)
        self.control(structList[i], i)

    def search(self, key):
        structList = self.structList
        index = self.index(key)
        print("Valore assegnato alla chiave",key, ":", structList[index].search(key))

    def index(self, key):

        for i in range(0, self.d):
            if key >= ((self.min) + (i * self.b)) and key < ((self.min) + (i + 1) * self.b):
                return i
            elif key < self.min:
                return self.d
            elif key > self.max:
                return self.d + 1
        exit()

    def control(self, struct, i):
        if type(struct) == LinkedListDictionary and struct.lenght() >= 6:
            return self.listToAVL(struct, i)
        elif type(struct) == AVLTree and struct.tree.n < 6:
            return self.AVLToList(struct, i)

    def listToAVL(self, struct, i):
        l = []
        current = struct.theList.first
        while current != None:
            l.append(current.elem)
            current = current.next
        self.structList.pop(i)
        self.structList.insert(i, AVLTree())
        for j in l:
            key = j[0]
            value = j[1]
            self.structList[i].insert(key, value)

    def AVLToList(self, struct, i):
        tree = BinaryTree()
        stack = PilaArrayList()
        l = []
        if struct.tree.root is not None:
            stack.push([struct.tree.root, 0])
        while not stack.isEmpty():
            current = stack.pop()
            level = current[1]
            l.append(current[0].info)
            if current[0].rightSon is not None:
                stack.push([current[0].rightSon, level + 1])
            if current[0].leftSon is not None:
                stack.push([current[0].leftSon, level + 1])
        self.structList.pop(i)
        self.structList.insert(i, LinkedListDictionary())
        for j in l:
            key = j[0]
            value = j[1]
            self.structList[i].insert(key, value)

    """
    ESEMPIO DI UTILIZZO
    """


if __name__ == "__main__":
    v = Structure(20, 100, 8)
    v.arrayPrint()

    for i in range(0, 120, 8):
        v.insert(i, i * 2)
    v.structPrint()

    for i in range(0, 120, 8):
        v.search(i)

    for i in range(60, 100):
        v.insert(i, i * 2)
    v.structPrint()

    for i in range(0, 120, 8):
        v.search(i)

    for i in range(60, 100):
        v.delete(i)
    v.structPrint()