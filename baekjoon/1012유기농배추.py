import sys
sys.setrecursionlimit(10**8)
sys.stdin = open("in1.txt","r")

t = int(input())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
answer = []
def DFS(x,y):
        board[x][y] = 0
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0<=tx<n and 0<=ty<m and board[tx][ty] == 1:
                DFS(tx,ty)

for _ in range(t):
    m,n,k = map(int,input().split())
    board = [[0]*m for _ in range(n)]
    for _ in range(k):
        i,j = map(int,input().split())
        board[j][i] = 1
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                cnt += 1
                DFS(i,j)
    answer.append(cnt)
     
for x in answer:
    print(x)