from collections import deque
graph = [[1,0,1,0,1,0],
         [1,1,1,1,1,1],
         [0,0,0,0,0,1],
         [1,1,1,1,1,1],
         [1,1,1,1,1,1]]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#1. 첫번째 값 queue에 집어넣기
def bfs(x, y):
    queue = deque()
    queue.append((x,y))
            
#2. while문을 통해 queue에서 뺀다.
    while queue:
        x, y = queue.popleft()
         
#3. 상하좌우 이동하기
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
#4. 벽에 부딪히거나 1일때 다음 포문 진행
            if nx < 0 or ny < 0 or nx >= len(graph) or ny >= len(graph[0]):
                continue
            if graph[nx][ny] == 0:
                continue

#5. 조건에 맞으면 graph값 변경 후 queue에 추가한다.
            if graph[nx][ny] == 1:
                graph[nx][ny] =  graph[x][y] + 1
                queue.append((nx, ny))
    return graph[len(graph)-1][len(graph[0])-1]

print(bfs(0, 0))
#print(len(graph[0]))
