class Graph_dls:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType = graphType

    def print_path(self, tracepath):
        for t in tracepath:
            print(t, end=" ")
        print()  # Add a newline after printing the path

    def dls(self, start_node, goal_node, depth_limit):
        if self.graphType == "Undirected Graph":
            return self.depth_limited_search_undirected(start_node, goal_node, depth_limit)
        else:
            return self.depth_limited_search_directed(start_node, goal_node, depth_limit)

    def depth_limited_search_undirected(self, current_vertex, goal_node, depth_limit, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(current_vertex)
        path.append(current_vertex)

        if current_vertex in goal_node:
            return path

        if depth_limit == 0:
            path.pop()
            return []

        neighbors = self.graph[current_vertex]

        for neighbor in neighbors:
            if neighbor not in visited:
                result = self.depth_limited_search_undirected(
                    neighbor, goal_node, depth_limit - 1, visited, path
                )
                if result:
                    return result

        path.pop()
        return []

    def depth_limited_search_directed(self, current_vertex, goal_node, depth_limit, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(current_vertex)
        path.append(current_vertex)

        if current_vertex in goal_node:
            return path

        if depth_limit == 0:
            path.pop()
            return []

        neighbors = self.graph[current_vertex]

        for neighbor in neighbors:
            if neighbor not in visited:
                result = self.depth_limited_search_directed(
                    neighbor, goal_node, depth_limit - 1, visited, path
                )
                if result:
                    return result

        path.pop()
        return []
