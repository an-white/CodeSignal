def getCentury(year):
    if year == 0:
        cetury = year // 100
    else:
        cetury = (year - 1) // 100 + 1
    return cetury


print(getCentury(0))
