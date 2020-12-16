import queue
from math import sqrt
inf = float('inf')

class AStar:
    def __init__(self, n, adj, cost, x, y):
        self.num = n
        self.adj = adj
        self.cost = cost
        self.distance = [inf]*n
        self.visited = [False]*n
        self.workset = []

        # Coordinates of the nodes
        self.x_cord = x
        self.y_cord = y

        # Destination and Potential Function
        self.dest_2d = None
        self.constant = 0

    def clear(self, src, dest):
        '''Summary of clear method
        Parameters:
        src (int): source node in array
        dest (int): destination node in array
        Returns:
        None
        '''
        self.distance = [inf]*self.num
        for vert in self.workset:
            self.visited[vert] = False
        del self.workset[0:]
        src_2d = (self.x_cord[src], self.y_cord[src])
        self.dest_2d = (self.x_cord[dest], self.y_cord[dest])
        self.constant = sqrt((src_2d[0]-self.dest_2d[0])**2 + (src_2d[1]-self.dest_2d[1])**2)

    def visit(self, node_que, index, prev):
        '''Summary of visit method
        Parameters:
        node_que (queue.PriorityQueue): heap containing unprocessed nodes
        index (int): current node being relaxed
        Returns:
        None
        '''
        self.visited[index] = True
        distance, adj, cost = self.distance, self.adj, self.cost
        self.workset.append(index)
        for vert in range(len(adj[index])):
            if distance[adj[index][vert]] > distance[index] + cost[index][vert]:
                distance[adj[index][vert]] = distance[index] + cost[index][vert]
                prev[adj[index][vert]] = index
                node_que.put((self.potential(adj[index][vert]), adj[index][vert]))

    def potential(self, vert):
        '''Summary of potential method
        Parameters:
        vert (int): node to get potential
        Returns:
        int: Potential Distance to Destination
        '''
        part = sqrt((self.x_cord[vert]-self.dest_2d[0])**2 + (self.y_cord[vert]-self.dest_2d[1])**2)
        return self.distance[vert] - self.constant + part

    def get_path(self, prev, node):
        '''Summary of get_path method
        Parameters:
        prev (list): source node in array
        node (int): destination node in array
        Returns:
        list: Path from node to source
        '''
        result = []
        while node is not None:
            result.append(node)
            node = prev[node]
        return result[::-1]
    
    def query(self, src, dest):
        '''Summary of query method
        Parameters:
        src (int): source node in array
        dest (int): destination node in array
        Returns:
        int: Shortest Distance if exists else -1
        '''
        self.clear(src, dest)
        node_que = queue.PriorityQueue()
        self.distance[src] = 0
        node_que.put((self.potential(src), src))
        journey = []
        prev = [None] * self.num
        while not node_que.empty():
            try:
                _, index = node_que.get_nowait()
                while self.visited[index]:
                    _, index = node_que.get_nowait()
            except queue.Empty:
                break
            self.visit(node_que, index, prev)
            journey.append(index)
            if self.visited[dest]:
                break
        if self.distance[dest]<inf: 
            return self.get_path(prev, dest), journey
        return -1, journey