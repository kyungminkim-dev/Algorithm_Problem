# from collections import deque
# m,n = map(int,input().split())
# board = [list(map(int,list(input()))) for _ in range(n)]

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# dist = [[-1]*m for _ in range(n)]
# dist[0][0] = 0
# q = deque()
# q.append((0,0))

# while q:
#     temp = q.popleft()
#     for i in range(4):
#         tx = temp[0] + dx[i]
#         ty = temp[1] + dy[i]
#         if 0<=tx<n and 0<=ty<m and dist[tx][ty] == -1:
#             if board[tx][ty] == 0:
#                 q.appendleft((tx,ty))
#                 dist[tx][ty] = dist[temp[0]][temp[1]]
#             else:
#                 q.append((tx,ty))
#                 dist[tx][ty] = dist[temp[0]][temp[1]] + 1

# print(dist[n-1][m-1])

import heapq
q = []
heapq.heappush(q,[0,0])
heapq.heappush(q,[1,0])
heapq.heappush(q,[2,0])
for i in range(3):
    print(heapq.heappop(q))

