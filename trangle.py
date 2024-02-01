def triangle(tri):
    pre_min_dists = []
    pre_min_dists.append(tri[0][0])
    depth = len(tri)
    for i in range(1, depth):
        cur_min_dists = []
        for j in range(i + 1):
            if j == 0:
                cur_min_dists.append(pre_min_dists[0] + tri[i][j])
            elif j == i:
                cur_min_dists.append(pre_min_dists[-1] + tri[i][j])
            else:
                cur_min_dists.append(min(pre_min_dists[j - 1], pre_min_dists[j]) + tri[i][j])
        pre_min_dists = cur_min_dists
    
    return min(pre_min_dists)