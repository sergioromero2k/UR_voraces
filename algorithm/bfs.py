from collections import deque

def bfs_aux(v, g, visited):
    visited[v] = True
    print(v, end= " ")
    q = deque()
    q.append(v)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                visited[adj] = True
                q.append(adj)
                print(adj, end = " ")
