def max_rect(matrix):
    m = len(matrix)
    n=len(matrix[0])
    dp_width = [[0]* n for _ in range(m)]
    dp_height = [[0]* n for _ in range(m)]
    max_area = 0
    dp_width[0][0] = int(matrix[0][0])
    dp_height[0][0] = int(matrix[0][0])
    for i in range(1, m):
        if matrix[i][0] == 0:
            continue
        dp_height[i][0] = 1 + dp_height[i-1][0]
        dp_width[i][0] = 1
    
    for j in range(1, n):
        if matrix[0][j] == 0:
            continue
        dp_width[0][j] = 1 + dp_height[0][j-1]
        dp_height[0][j] = 1
    
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == '0':
                continue
            top_height = dp_height[i-1][j]
            top_width = dp_width[i-1][j]
            left_height = dp_height[i][j-1]
            left_width = dp_width[i][j-1]
            top_left_height = dp_height[i-1][j-1]
            top_left_width = dp_width[i-1][j-1]
            cur_width = 1 + min(top_width - 1, left_width, top_left_width)
            cur_height = 1 + min(top_height, left_height - 1, top_left_height)
            dp_width[i][j] = cur_width
            dp_height[i][j] = cur_height
    
    for i in range(m):
        for j in range(n):
            max_area = max(max_area, dp_width[i][j] * dp_height[i][j])
    return max_area
max_rect([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
    

