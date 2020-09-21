from collections import deque
n, k = map(int,input().split())

dy = [0]*100001
ch = [0]*100001
ch[n] = 1
q = deque()
q.append(n)
answer = 0
while q:
    temp = q.popleft()
    if temp == k:
        answer = dy[k]
        break
    for i in (temp-1, temp+1, temp*2):
        if 0<=i<=100000:
            if ch[i] == 0:
                dy[i] = dy[temp] + 1
                q.append(i)
                ch[i] = 1

print(answer)
