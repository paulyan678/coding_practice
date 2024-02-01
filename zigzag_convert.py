def convert(string, numRows):
    if numRows == 1:
        return string
    rows = ['']*numRows
    cur_row = 0
    countDown = False
    for char in string:
        rows[cur_row] += char
        if cur_row == numRows - 1:
            countDown = True
        elif cur_row == 0:
            countDown = False
        
        if countDown:
            cur_row -= 1
        else:
            cur_row += 1

    res = ''
    for row in rows:
        res += row
    return res

print(convert("PAYPALISHIRING", numRows = 3))