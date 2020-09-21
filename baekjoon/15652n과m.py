n,m = map(int,input().split())

res = [0]*m

def DFS(v,s):
    if v == m:
        for k in res:
            print(k,end= ' ')
        print()
    else:
        for i in range(s,n+1):
            res[v] = i
            DFS(v+1,i)

DFS(0,1)