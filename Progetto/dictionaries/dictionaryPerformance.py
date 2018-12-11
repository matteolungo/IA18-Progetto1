from dictTrees.binarySearchTree import BinarySearchTree
from dictTrees.avlTree import AVLTree
from dictionaries.linkedListDictionary import LinkedListDictionary

from time import time


def dictionaryPerformance(ops, dic):
    start = time()
    for i in range(ops):
        dic.insert(i, i + 10)
    elapsed = time() - start
    print(f"Tempo totale per {ops} operazioni di INSERT: {elapsed} s")
    print("Tempo medio INSERT:", elapsed / ops, " s")

    start = time()
    for i in reversed(range(ops)):
        dic.search(i)
    elapsed = time() - start
    print(f"Tempo totale per {ops} operazioni di SEARCH: {elapsed} s")
    print("Tempo medio SEARCH:", elapsed / ops, " s")

    start = time()
    for i in range(ops):
        dic.delete(i)
    elapsed = time() - start
    print(f"Tempo totale per {ops} operazioni di DELETE: {elapsed} s")
    print("Tempo medio DELETE:", elapsed / ops, " s")


if __name__ == "__main__":
    ops = 100

    ll = LinkedListDictionary()
    print("LINKED LIST DICTIONARY")
    dictionaryPerformance(ops, ll)

    bst = BinarySearchTree()
    print("BINARY SEARCH TREE")
    dictionaryPerformance(ops, bst)

    avl = AVLTree()
    print("AVL TREE")
    dictionaryPerformance(ops, avl)