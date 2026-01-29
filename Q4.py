import sys
n = int(sys.argv[1]) if len(sys.argv) > 1 else 8

visited = [[False] * n for _ in range(n)]

def is_valid_move(x, y):
    return 0 <= x < n and 0 <= y < n and not visited[x][y]

def knight_tour(x, y):
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    from collections import deque
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True
    prev = {(x, y): None}

    ans = -1 
    while q:
        x, y, step = q.popleft()
  
        for dx, dy in moves:
            xx, yy = x + dx, y + dy
            if is_valid_move(xx, yy):
                visited[xx][yy] = True
                q.append((xx, yy, step + 1))
                prev[(xx, yy)] = (x, y)
                if xx == n - 1 and yy == n - 1:
                    ans = step + 1
                    break
        if ans != -1:
            break
    if ans == -1:
        print(-1)
    else:
        print(ans)
        path = []
        def dfs(x, y):
            if prev[(x, y)] is None:
                path.append(f"({x + 1}, {y + 1})")
                return
            dfs(prev[(x, y)][0], prev[(x, y)][1])
            path.append(f"({x + 1}, {y + 1})")
        dfs(n - 1, n - 1)
        print(" -> ".join(path))

if n == 1:
    print(0)
    print("(1, 1)")
else:
  knight_tour(0, 0)