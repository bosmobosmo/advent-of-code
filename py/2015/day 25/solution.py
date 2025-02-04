def find_code(row: int, column: int) -> int:
    code = 20151125
    cur_row = 1
    cur_column = 1
    max_row = 1
    while cur_row < row or cur_column < column:
        code = (code * 252533) % 33554393
        if cur_row == 1:
            max_row += 1
            cur_row = max_row
            cur_column = 1
        else:
            cur_row -= 1
            cur_column += 1
    return code
