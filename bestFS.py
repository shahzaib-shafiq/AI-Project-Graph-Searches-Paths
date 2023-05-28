import heapq

class Graph_bestfs:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType = graphType

    def print_path(self, tracepath):
        for t in tracepath:
            print(t, end=" ")
        print()  # Add a newline after printing the path

    def bfs(self, start_node, goal_node, heuristic):
        if self.graphType == "Undirected Graph":
            return self.best_first_search_undirected(start_node, goal_node, heuristic)
        else:
            return self.best_first_search_directed(start_node, goal_node, heuristic)

    def best_first_search_undirected(self, start_node, goal_node, heuristic):
        visited = set()
        priority_queue = [(heuristic(start_node), start_node, [start_node])]  # (heuristic_value, node, path)

        while priority_queue:
            _, current_node, path = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node in goal_node:
                return path

            neighbors = self.graph[current_node]

            for neighbor in neighbors:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (heuristic(neighbor), neighbor, new_path))

        return []

    def best_first_search_directed(self, start_node, goal_node, heuristic):
        visited = set()
        priority_queue = [(heuristic(start_node), start_node, [start_node])]  # (heuristic_value, node, path)

        while priority_queue:
            _, current_node, path = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node in goal_node:
                return path

            neighbors = self.graph[current_node]

            for neighbor in neighbors:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (heuristic(neighbor), neighbor, new_path))

        return []
