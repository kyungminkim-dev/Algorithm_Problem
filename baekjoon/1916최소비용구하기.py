import heapq
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = {}
for i in range(n):
    graph[i+1] = {}

for i in range(m):
    s,e,v = map(int,sys.stdin.readline().split())
    if e in graph[s]:
        graph[s][e] = min(graph[s][e],v)
    else:
        graph[s][e] = v

s,e = map(int,sys.stdin.readline().split())

def dijkstra(graph,start):

    distances = {node : float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue,[distances[start], start])

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

dist = dijkstra(graph,s)
print(dist[e])



