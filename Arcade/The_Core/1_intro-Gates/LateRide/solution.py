def solution(n):
    total = 0
    for i in list(str(n // 60)):
        total += int(i)
    for j in list(str(n % 60)):
        total += int(j)

    return total


print(solution(808))


## the fastest sol
def fastSolution(n):
    return sum(map(int, str(n // 60 * 100 + n % 60)))
