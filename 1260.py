N, M, V = map(int, input().split())

array = [[0] * (N + 1) for i in range(N + 1)]
visit = [0 for i in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    array[a][b] = array[a][b] = 1


def dfs(V):
    print(V, end=' ')
    visit[V] = 1
    for i in range(1, N + 1):
        if visit[i] == 0 and array[V][i] == 1:
            dfs(i)

def bfs(V):
    queue = [V]
    visit[V] = 0
    while(queue):
        V = queue[0]
        print(V, end=' ')
        del queue[0]
        for i in range(1, N + 1):
            if visit[i] == 1 and array[V][i] == 1:
                queue.append(i)
                visit[i] = 0

dfs(V)
print()
bfs(V)