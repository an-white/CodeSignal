def firstDuplicate(a):
    vals = set()
    for i in a:
        if i in vals:
            return i
        vals.add(i)
    return -1
