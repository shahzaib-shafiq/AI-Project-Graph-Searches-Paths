import heapq

class Graph_Astar:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType = graphType

    def print_path(self, tracepath):
        for p in tracepath:
            print(p, end=" ")
        print()  # Add a newline after printing the path

    def astar(self, start_node, goal_node, heuristic, cost_function):
        if self.graphType == "Undirected Graph":
            return self.astar_undirected(start_node, goal_node, heuristic, cost_function)
        else:
            return self.astar_directed(start_node, goal_node, heuristic, cost_function)

    def astar_undirected(self, start_node, goal_node, heuristic, cost_function):
        visited = set()
        priority_queue = [(0 + heuristic(start_node), 0, start_node, [start_node])]  # (f_value, g_value, node, path)

        while priority_queue:
            _, g_value, current_node, path = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node in goal_node:
                return path

            neighbors = self.graph[current_node]

            for neighbor in neighbors:
                if neighbor not in visited:
                    new_g_value = g_value + cost_function(current_node, neighbor)
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (new_g_value + heuristic(neighbor), new_g_value, neighbor, new_path))

        return []

    def astar_directed(self, start_node, goal_node, heuristic, cost_function):
        visited = set()
        priority_queue = [(0 + heuristic(start_node), 0, start_node, [start_node])]  # (f_value, g_value, node, path)

        while priority_queue:
            _, g_value, current_node, path = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node in goal_node:
                return path

            neighbors = self.graph[current_node]

            for neighbor in neighbors:
                if neighbor not in visited:
                    new_g_value = g_value + cost_function(current_node, neighbor)
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (new_g_value + heuristic(neighbor), new_g_value, neighbor, new_path))

        return []