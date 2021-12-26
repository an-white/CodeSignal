def solution(grid):
    for i in range(9):
        vals_in_row = set()
        for j in range(9):
            if grid[i][j] not in vals_in_row:
                vals_in_row.add(grid[i][j])
            elif grid[i][j] != "." and grid[i][j] in vals_in_row:
                return False

    for j in range(9):
        vals_in_col = set()
        for i in range(9):
            if grid[i][j] != "." and grid[i][j] not in vals_in_col:
                vals_in_col.add(grid[i][j])
            elif grid[i][j] != "." and grid[i][j] in vals_in_col:
                return False

    for sub_x in range(0, 9, 3):
        for sub_y in range(0, 9, 3):
            vals_in_sub = set()
            for i in range(sub_x, sub_x + 3, 1):
                for j in range(sub_y, sub_y + 3, 1):
                    if grid[i][j] != "." and grid[i][j] not in vals_in_sub:
                        vals_in_sub.add(grid[i][j])
                    elif grid[i][j] != "." and grid[i][j] in vals_in_sub:
                        return False
    return True


grid = [
    ["1", ".", ".", "2", ".", ".", "4", ".", "."],
    [".", ".", "3", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", "6", ".", "."],
    [".", ".", "7", ".", "1", ".", "3", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["7", ".", ".", "8", ".", ".", "9", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "."],
    [".", ".", ".", ".", ".", "5", "2", ".", "."],
]
print(solution(grid))
