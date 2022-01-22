from collections import deque
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited = [False] * 9
queue = deque()
def bfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            queue.append(i)
    if len(queue) == 0:
        return
    bfs(graph, queue.popleft(), visited)
    





bfs(graph, 1, visited)
