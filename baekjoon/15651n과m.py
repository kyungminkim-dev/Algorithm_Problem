n,m = map(int,input().split())

res = [0]*m

def DFS(v):
    if v == m:
        for k in res:
            print(k, end= ' ')
        print()
    else:
        for i in range(1,n+1):
            res[v] = i
            DFS(v+1)

DFS(0)