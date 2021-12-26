def solution(arr):
    arr.sort()
    c = 0
    for i in arr:
        if c != i:
            return c
        c += 1
    return c
