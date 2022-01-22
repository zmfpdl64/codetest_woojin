graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited = [False] * 9

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)
            

dfs(graph, 1, visited)

#1. 인접한 노드 리스트
#2. 방문 여부 리스트
#3. 재귀함수
