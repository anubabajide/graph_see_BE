from collections import deque
from heapq import heappush, heapify, heappop
inf = float('inf')

def get_path(prev, node):
    result = []
    while node is not None:
        result.append(node)
        node = prev[node]
    return result[::-1]

def find_distance(adj, cost, s, t):
    num_nodes = len(adj)
    dist = [inf] * num_nodes
    prev = [None] * num_nodes
    seen = [False] * num_nodes
    journey = []

    dist[s] = 0
    priority_queue = [(dist[i], i) for i in range(num_nodes)]
    heapify(priority_queue)
    
    for _x in range(num_nodes):
        _, index = heappop(priority_queue)
        while seen[index]:
            _, index = heappop(priority_queue)
        seen[index] = True
        journey.append(index)

        for i in range(len(adj[index])):
            if dist[adj[index][i]] > dist[index] + cost[index][i]:
                dist[adj[index][i]] = dist[index] + cost[index][i]
                prev[adj[index][i]] = index
                heappush(priority_queue, (dist[adj[index][i]], adj[index][i]))

        if seen[t]:
            break
    if dist[t] < inf: 
        return get_path(prev, t), journey
    return -1, journey
