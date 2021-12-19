def solution(s):
    old_vals = set()
    for char in s:
        if (char not in old_vals) and (s.count(char)) == 1:
            return char
        old_vals.add(char)
    return "_"


# the fastest answer
def fast_sol(s):
    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return "_"
