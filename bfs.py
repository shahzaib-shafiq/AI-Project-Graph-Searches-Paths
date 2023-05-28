from collections import deque

class Graph_bfs:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType = graphType

    def print_path(self, tracepath):
        for t in tracepath:
            print(t, end=" ")
        print()  # Add a newline after printing the path

    def bfs(self, start_node, goal_node):
        if self.graphType == "Undirected Graph":
            return self.breadth_first_search_undirected(start_node, goal_node)
        else:
            return self.breadth_first_search_directed(start_node, goal_node)

    def breadth_first_search_undirected(self, start_vertex, goal_node):
        visited = set()
        queue = deque([(start_vertex, [start_vertex])])

        while queue:
            vertex, path = queue.popleft()
            visited.add(vertex)

            if vertex in goal_node:
                return path

            neighbors = self.graph[vertex]

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        return []

    def breadth_first_search_directed(self, start_vertex, goal_node):
        visited = set()
        queue = deque([(start_vertex, [start_vertex])])

        while queue:
            vertex, path = queue.popleft()
            visited.add(vertex)

            if vertex in goal_node:
                return path

            neighbors = self.graph[vertex]

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        return []
