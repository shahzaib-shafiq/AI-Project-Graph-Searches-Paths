import heapq

class Graph_ucs:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType = graphType

    def print_path(self, tracepath):
        for t in tracepath:
            print(t, end=" ")
        print()  # Add a newline after printing the path

    def ucs(self, start_node, goal_node):
        if self.graphType == "Undirected Graph":
            return self.uniform_cost_search_undirected(start_node, goal_node)
        else:
            return self.uniform_cost_search_directed(start_node, goal_node)

    def uniform_cost_search_undirected(self, start_node, goal_node):
        visited = set()
        priority_queue = [(0, start_node, [start_node])]  # (cumulative_cost, node, path)

        while priority_queue:
            cumulative_cost, current_node, path = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node in goal_node:
                return path

            neighbors = self.graph[current_node]

            for neighbor, cost in neighbors.items():
                if neighbor not in visited:
                    new_cumulative_cost = cumulative_cost + cost
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (new_cumulative_cost, neighbor, new_path))

        return []

    def uniform_cost_search_directed(self, start_node, goal_node):
        visited = set()
        priority_queue = [(0, start_node, [start_node])]  # (cumulative_cost, node, path)

        while priority_queue:
            cumulative_cost, current_node, path = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node in goal_node:
                return path

            neighbors = self.graph[current_node]

            for neighbor, cost in neighbors.items():
                if neighbor not in visited:
                    new_cumulative_cost = cumulative_cost + cost
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (new_cumulative_cost, neighbor, new_path))

        return []
