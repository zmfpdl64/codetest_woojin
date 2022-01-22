graph = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]
count = 0
def dfs(x, y):
    if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[0]):
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x-1, y)
        dfs(x, y+1)
        return True
    return False

for i in range(len(graph)):
    for j in range(len(graph[0])):
        if dfs(i, j):
            count += 1

print(count)
    
    
