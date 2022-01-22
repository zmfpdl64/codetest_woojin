#1, 좌표생성
#2. 
def solution(st):
    st = list(st)
    dx = [2, 2, -2, -2, -1, 1, -1, 1]
    dy = [1, -1, 1, -1, 2, 2, -2, -2]
    count = 0
    for i in range(len(dx)):
        if (ord(st[0]) - dx[i]) >= ord('a') and (ord(st[0]) - dx[i]) <= ord('g')\
        and int(st[1])+dy[i] >= 1 and int(st[1]) + dy[i] <= 8:
            count += 1    
    print(count)


solution('d1')
