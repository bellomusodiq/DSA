from data_structures.queue import Queue
from data_structures.stack import Stack

class Graph:
    
    def __init__(self, directed=False):
        
        self.adjacency = {}
        self.directed = directed
        
    def add_vertex(self, vertex):
        
        if vertex not in self.adjacency:
            self.adjacency[vertex] = set()
            
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        
        self.adjacency[vertex1].add(vertex2)
        if not self.directed:
            self.adjacency[vertex2].add(vertex1)
        
    def has_vertex(self, vertex):
        return vertex in self.adjacency
    
    def has_edge(self, vertex1, vertex2):
        if not self.has_vertex(vertex1):
            return False
        return vertex2 in self.adjacency[vertex1]
    
    def neighbors(self, vertex):
        if not self.has_vertex(vertex):
            return set()
        return self.adjacency[vertex].copy()
    
    def degree(self, vertex):
        if not self.has_vertex(vertex):
            return 0
        return len(self.adjacency[vertex])
    
    def out_degree(self, vertex):
        if not self.has_vertex(vertex):
            return 0
        return len(self.adjacency[vertex])
    
    def in_degree(self, vertex):
        if not self.has_vertex(vertex):
            return 0
        count = 0
        for neighbors in self.adjacency.values():
            if vertex in neighbors:
                count += 1
        return count
    
    def remove_edge(self, vertex1, vertex2):
        if not self.has_edge(vertex1, vertex2):
            return False
        self.adjacency[vertex1].discard(vertex2)
        if not self.directed:
            self.adjacency[vertex2].discard(vertex1)
        return True
        
    def remove_vertex(self, vertex):
        if not self.has_vertex(vertex):
            return False
        
        for neighbors in self.adjacency.values():
            neighbors.discard(vertex)
            
        del self.adjacency[vertex]
        return True
    
    def bfs(self, start):
        if not self.has_vertex(start):
            return []
        q = Queue()
        visited = set({start})
        result = []
                
        q.enqueue(start)
        
        while q.can_dequeue:
            vertex = q.pop()
            result.append(vertex)
            
            for neighbor in self.neighbors(vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.enqueue(neighbor)
                    
        
        return result
    
    def dfs(self, start):
        if not self.has_vertex(start):
            return []
        stack = Stack()
        visited = set({start})
        stack.push(start)
        results = []
        
        while stack.can_pop:
            vertex = stack.pop()
            results.append(vertex)
            for neighbor in self.neighbors(vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.push(neighbor)
                    
        return results
    
    def dfs_recursive(self, vertex, visited=None, result=None):
        if not self.has_vertex(vertex):
            return []
        
        if visited is None:
            visited = set()
            result = []
            
        visited.add(vertex)
        result.append(vertex)
        
        for neighbor in self.neighbors(vertex):
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited, result)
                
        return result

    def has_path(self, start, end):
        if not self.has_vertex(start) or not self.has_vertex(end):
            return False

        Q = Queue()
        visited = {start}
        Q.enqueue(start)
        
        while Q.can_dequeue:
            current = Q.pop()
            if current == end:
                return True
            for neighbor in self.neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    Q.enqueue(neighbor)
                    
        return False
    
    def shortest_path(self, start, end):
        if not self.has_vertex(start) or not self.has_vertex(end):
            return None
        
        queue = Queue()
        queue.enqueue(start)
        previous = {start: None}
        
        while queue.can_dequeue:
            current = queue.pop()
            
            if current == end:
                break
            
            for neighbor in self.neighbors(current):
                if neighbor not in previous:
                    previous[neighbor] = current
                    queue.enqueue(neighbor)

        if end not in previous:
            return None

        path = []
        current = end

        while current is not None:
            path.append(current)
            current = previous[current]

        path.reverse()
        return path
            
    
    def __str__(self):
        return str(self.adjacency)
