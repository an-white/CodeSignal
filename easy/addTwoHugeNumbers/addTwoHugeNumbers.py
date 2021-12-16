def get_num(num):
    str_numeric = ""
    for i in num:
        str_numeric += f"{'0' * (4 - len(str(i)))}{i}"

    return int(str_numeric)


def addTwoHugeNumbers(a, b):

    a_num = get_num(a)
    b_num = get_num(b)

    sum = str(a_num + b_num)
    sum = sum[-1::-1]

    ret_list = []
    for i in range(0, len(sum), 4):
        ret_list.append(int(sum[i : i + 4][-1::-1]))

    return ret_list[-1::-1]


addTwoHugeNumbers([9876, 5432, 1999], [1, 8001])

addTwoHugeNumbers([123, 4, 5], [100, 100, 100])
