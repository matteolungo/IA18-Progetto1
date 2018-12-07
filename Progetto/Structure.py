"""
    File name: array.py
    Author: Matteo Lungo
    Date created: 05/12/2018
    Date last modified: 14/12/2018
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
        print(structList[index].search(key))

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
        l=[]
        tree = BinaryTree()
        struct.tree = tree
        tree.stack = PilaArrayList()
        s = tree.stack.s
        if tree.root is not None:
            stack.push([tree.root, 0])
        while not tree.stack.isEmpty():
            current = stack.pop()
            level = current[1]
            if current[0].rightSon is not None:
                stack.push([current[0].rightSon, level + 1])
            if current[0].leftSon is not None:
                stack.push([current[0].leftSon, level + 1])
        for i in s:
            l.append(i)
        self.structList.pop(i)
        self.structList.insert(i, LinkedListDictionary())
        for j in l:
            key = j[0]
            value = j[1]
            self.structList[i].insert(key, value)


if __name__ == "__main__":
    v = Structure(5, 40, 7)
    v.arrayPrint()

    v.insert(10, 20)
    v.insert(20, 30)
    v.insert(30, 40)
    v.structPrint()

    v.insert(10, 20)
    v.insert(10, 20)
    v.insert(10, 20)
    v.insert(10, 20)
    v.insert(10, 20)
    v.structPrint()

    v.delete(10)
    v.structPrint()
