import heapq
import sys
n,m,x = map(int,sys.stdin.readline().split())

graph = {}
for i in range(n):
    graph[i+1] = {}

for i in range(m):
    s,e,v = map(int,sys.stdin.readline().split())
    if e in graph[s]:
        graph[s][e] = min(graph[s][e],v)
    else:
        graph[s][e] = v
    
def djikstra(graph,start):
    distances = {node : float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue,[distances[start],start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue,[distance,adjacent])

    return distances

res = float('-inf')
back_distances = djikstra(graph,x)

for i in range(1,n+1):
    temp = back_distances[i]
    distances = djikstra(graph,i)
    temp += distances[x]
    if temp > res:
        res = temp
print(res)




