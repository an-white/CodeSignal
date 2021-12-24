def solution(a):
    list_of_tuples = zip(*a[::-1])
    return [list(elem) for elem in list_of_tuples]


# the best solution
def solution(a):
    return list(zip(*reversed(a)))
