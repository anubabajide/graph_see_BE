from collections import deque
from heapq import heappush, heapify, heappop
inf = float('inf')

def get_path(prev, node):
    result = []
    while node is not None:
        result.append(node)
        node = prev[node]
    return result[::-1]

def distance(adj, cost, s, t):
    dist = [inf] * len(adj)
    prev = [None] * len(adj)
    seen = [False] * len(adj)
    journey = [0] * len(adj)
    dist[s] = 0
    priority_queue = [(dist[i], i) for i in range(len(adj))]
    heapify(priority_queue)
    
    for x in range(len(adj)):
        _, index = heappop(priority_queue)
        while seen[index]:
            _, index = heappop(priority_queue)
        seen[index] = True
        journey[x] = index

        for i in range(len(adj[index])):
            if dist[adj[index][i]] > dist[index] + cost[index][i]:
                dist[adj[index][i]] = dist[index] + cost[index][i]
                prev[adj[index][i]] = index
                heappush(priority_queue, (dist[adj[index][i]], adj[index][i]))

        if seen[t]:
            del journey[x+1:]
            if dist[t] < inf: 
                return get_path(prev, t), journey
            else:
                return -1, journey
    return -1
