class Graph_bidirectional:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType = graphType

    def print_path(self, tracepath):
        for t in tracepath:
            print(t, end=" ")
        print()  # Add a newline after printing the path

    def bidirectional_search(self, start_node, goal_node):
        if self.graphType == "Undirected Graph":
            return self.bidirectional_search_undirected(start_node, goal_node)
        else:
            return self.bidirectional_search_directed(start_node, goal_node)

    def bidirectional_search_undirected(self, start_node, goal_node):
        forward_visited = set()
        backward_visited = set()
        forward_path = []
        backward_path = []

        forward_queue = [start_node]
        backward_queue = [goal_node]

        while forward_queue and backward_queue:
            current_forward = forward_queue.pop(0)
            current_backward = backward_queue.pop(0)

            forward_visited.add(current_forward)
            backward_visited.add(current_backward)

            forward_path.append(current_forward)
            backward_path.append(current_backward)

            if current_forward in backward_visited:
                intersect_node = current_forward
                forward_path.extend(backward_path[::-1])
                return forward_path

            if current_backward in forward_visited:
                intersect_node = current_backward
                backward_path.extend(forward_path[::-1])
                return backward_path

            forward_neighbors = self.graph[current_forward]
            backward_neighbors = self.graph[current_backward]

            for neighbor in forward_neighbors:
                if neighbor not in forward_visited:
                    forward_queue.append(neighbor)

            for neighbor in backward_neighbors:
                if neighbor not in backward_visited:
                    backward_queue.append(neighbor)

        return []

    def bidirectional_search_directed(self, start_node, goal_node):
        forward_visited = set()
        backward_visited = set()
        forward_path = []
        backward_path = []

        forward_queue = [start_node]
        backward_queue = [goal_node]

        while forward_queue and backward_queue:
            current_forward = forward_queue.pop(0)
            current_backward = backward_queue.pop(0)

            forward_visited.add(current_forward)
            backward_visited.add(current_backward)

            forward_path.append(current_forward)
            backward_path.append(current_backward)

            if current_forward in backward_visited:
                intersect_node = current_forward
                forward_path.extend(backward_path[::-1])
                return forward_path

            if current_backward in forward_visited:
                intersect_node = current_backward
                backward_path.extend(forward_path[::-1])
                return backward_path

            forward_neighbors = self.graph[current_forward]
            backward_neighbors = self.graph[current_backward]

            for neighbor in forward_neighbors:
                if neighbor not in forward_visited:
                    forward_queue.append(neighbor)

            for neighbor in backward_neighbors:
                if neighbor not in backward_visited:
                    backward_queue.append(neighbor)

        return []
