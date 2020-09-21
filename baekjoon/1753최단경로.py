import heapq
import sys
v,e = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())


graph = {}
for i in range(1,v+1):
    graph[i] = {}

for i in range(e):
    u,w,v = map(int,sys.stdin.readline().split())
    if w in graph[u]:
        graph[u][w] = min(graph[u][w],v)
    else:
        graph[u][w] = v

def dijkstra(graph,start):

    distances = {node : float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue
            
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance,adjacent])

    return distances

dist = dijkstra(graph,start)
for i,v in dist.items():
    if v == float('inf'):
        print("INF")
    else:
        print(v)


