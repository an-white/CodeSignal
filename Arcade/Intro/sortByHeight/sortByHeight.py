def sortByHeight(row):

    t = [i for i in range(len(row)) if row[i] == -1]
    persons = list(set(range(len(row))) - set(t))

    p_arr = [row[i] for i in persons]
    p_arr.sort()

    counter = 0
    for i in persons:
        row[i] = p_arr[counter]
        counter += 1

    return row


sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180])
