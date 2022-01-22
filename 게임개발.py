def solution(kmap):
    x, y = 1, 1
    count = 0
    wn = 0
    #바라보고있는 방향
    p = [0,1,2,3]
    dx = [-1,0, 1, 0]
    dy = [0, 1, 0, -1]
    while True:
        kmap[x][y] = 1
        for i in range(len(dx)):

            if kmap[y+dy[i]][x+dx[i]] == 0:
                x += dx[i]
                y += dy[i]
                kmap[y+dy[i]][x+dx[i]] = 1
                wn != 1
                break
            count += 1
        if count == 4:
            break
        count = 0

    print(wn)
            




solution([[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]])
