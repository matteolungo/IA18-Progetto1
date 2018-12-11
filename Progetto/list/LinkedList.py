"""
    File name: LinkedList.py
    Author: Domenico Spera
    Date created: 11/10/2016
    Modified By: Laura Trivelloni
    Modified By: Matteo Lungo
    Date last modified: 06/12/2018
    Python Version: 3.5.2

    This module implements a list_! where each item maintains a reference to the next one
    and methods to check if the list_! is empty, print all items, get the first/last item,
    add a new item at the top/bottom, visualize the item at the top/bottom.
"""


class Record:

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class ListaCollegata:

    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self):
        return (self.first == None)

    def getFirst(self):
        if self.first == None:
            return None
        else:
            return self.first.elem

    def getLast(self):
        if self.last == None:
            return None
        else:
            return self.last.elem

    def addAsLast(self, elem):
        rec = Record(elem)
        if self.first == None:
            self.first = self.last = rec
        else:
            self.last.next = rec
            self.last = rec

    def addAsFirst(self, elem):
        rec = Record(elem)
        if self.first == None:
            self.first = self.last = rec
        else:
            rec.next = self.first
            self.first = rec

    def popFirst(self):
        if self.first == None:
            return None
        else:
            res = self.first.elem
            self.first = self.first.next
            if self.first == None:
                self.last = None  # empty list_!
            return res

    # popLast e deleteRecord not efficient now

    def getFirstRecord(self):
        if self.first == None:
            return None
        else:
            return self.first

    def getLastRecord(self):
        if self.first == None:
            return None
        else:
            return self.last

    def printOrdered(self):
        if self.first == None:
            print("[]")
            return

        s = "["
        current = self.first
        while current != None:
            if len(s) > 1:
                s += ", "
            s += str(current.elem)
            current = current.next
        s += "]"
        print(s)

    def lenght(self):
        if self.first == None:
            return 0

        l = []
        current = self.first
        while current != None:
            l.append(current.elem)
            current = current.next
        return len(l)


# to run this module directly (NOT imported in another one)
if __name__ == "__main__":

    l = ListaCollegata()
    l.printOrdered()
    print(l.lenght())
    print("addAsFirst(2)")
    l.addAsFirst(2)
    print("addAsFirst(3)")
    l.addAsFirst(3)
    print("addAsLast(4)")
    l.addAsLast(4)
    l.printOrdered()
    print(l.lenght())
    print("getFirst()", l.getFirst())
    print("getLast()", l.getLast())
    l.printOrdered()
    print(l.lenght())
    print("popFirst()", l.popFirst())
    print("findFirst()=", l.getFirst())
    print("popFirst()", l.popFirst())
    print("popFirst()", l.popFirst())
    l.printOrdered()
    print(l.lenght())
    print("findLast()=", l.getLast())
