def removeKFromList(container, k):
    removedK = [container[n] for n in range(len(container)) if container[n] != k]

    return removedK


removeKFromList([3, 1, 2, 3, 4, 5], 3)
