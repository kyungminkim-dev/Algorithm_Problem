from collections import deque
m,n,h = map(int,input().split())
board= []
for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int,input().split())))
    board.append(temp)

dx = [-1,0,1,0]
dy = [0,1,0,-1]
dh = [-1,1]

q = deque()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if board[k][i][j] == 1:
                q.append((k,i,j))

cnt = 0
while q:
    size = len(q)
    for _ in range(size):
        temp = q.popleft()
        for i in range(4):
            tx = temp[1] + dx[i]
            ty = temp[2] + dy[i]
            if 0<=tx<n and 0<=ty<m and board[temp[0]][tx][ty] == 0:
                q.append((temp[0],tx,ty))
                board[temp[0]][tx][ty] = 1
        for k in range(2):
            th = temp[0] + dh[k]
            if 0<=th<h and board[th][temp[1]][temp[2]] == 0:
                q.append((th,temp[1],temp[2]))
                board[th][temp[1]][temp[2]] = 1
    if len(q): cnt += 1

for k in range(h):
    for i in range(n):
        for j in range(m):
            if board[k][i][j] == 0:
                cnt = -1
                break

if cnt == -1:
    print(-1)
else:
    print(cnt)