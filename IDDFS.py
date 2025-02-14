class Graph_iddfs:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType = graphType

    def print_path(self, tracepath):
        for t in tracepath:
            print(t, end=" ")
        print()  # Add a newline after printing the path

    def dfs(self, start_node, goal_node):
        if self.graphType == "Undirected Graph":
            return self.iterative_deepening_search_undirected(start_node, goal_node)
        else:
            return self.iterative_deepening_search_directed(start_node, goal_node)

    def iterative_deepening_search_undirected(self, start_node, goal_node):
        depth_limit = 0
        while True:
            result = self.depth_first_search_undirected(start_node, goal_node, depth_limit)
            if result:
                return result
            depth_limit += 1

    def iterative_deepening_search_directed(self, start_node, goal_node):
        depth_limit = 0
        while True:
            result = self.depth_first_search_directed(start_node, goal_node, depth_limit)
            if result:
                return result
            depth_limit += 1

    def depth_first_search_undirected(self, current_vertex, goal_node, depth_limit, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        if current_vertex in visited:
            return []

        visited.add(current_vertex)
        path.append(current_vertex)

        if current_vertex in goal_node:
            return path

        if depth_limit == 0:
            path.pop()
            return []

        neighbors = self.graph[current_vertex]

        for neighbor in neighbors:
            result = self.depth_first_search_undirected(
                neighbor, goal_node, depth_limit - 1, visited, path
            )
            if result:
                return result

        path.pop()
        return []

    def depth_first_search_directed(self, current_vertex, goal_node, depth_limit, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        if current_vertex in visited:
            return []

        visited.add(current_vertex)
        path.append(current_vertex)

        if current_vertex in goal_node:
            return path

        if depth_limit == 0:
            path.pop()
            return []

        neighbors = self.graph[current_vertex]

        for neighbor in neighbors:
            result = self.depth_first_search_directed(
                neighbor, goal_node, depth_limit - 1, visited, path
            )
            if result:
                return result

        path.pop()
        return []
