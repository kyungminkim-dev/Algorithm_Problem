from collections import deque
m,n = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]



dx = [-1,0,1,0]
dy = [0,1,0,-1]

q = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i,j))
cnt = 0

while q:
    size = len(q)
    for i in range(size):
        temp = q.popleft()
        for j in range(4):
            tx = temp[0] + dx[j]
            ty = temp[1] + dy[j]
            if 0<=tx<n and 0<=ty<m and board[tx][ty] == 0:
                board[tx][ty] = 1
                q.append((tx,ty))
    if(len(q)): cnt += 1

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            cnt = -1
            break
if cnt == -1:
    print(-1)
else:
    print(cnt)





