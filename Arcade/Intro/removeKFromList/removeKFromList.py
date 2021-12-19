def removeKFromList(container, k):
    removedK = [n for n in container if n != k]

    return removedK


removeKFromList([3, 1, 2, 3, 4, 5], 3)
