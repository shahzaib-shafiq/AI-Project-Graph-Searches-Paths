class Graph_AlphaBeta:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType = graphType

    def print_path(self, tracepath):
        for t in tracepath:
            print(t, end=" ")
        print()  # Add a newline after printing the path

    def alphabeta(self, start_node, goal_node):
        if self.graphType == "Undirected Graph":
            return self.alphabeta_undirected(start_node, goal_node)
        else:
            return self.alphabeta_directed(start_node, goal_node)

    def alphabeta_undirected(self, current_vertex, alpha, beta, is_max_player):
        if current_vertex in goal_node:
            return current_vertex

        if is_max_player:
            value = float('-inf')
            neighbors = self.graph[current_vertex]

            for neighbor in neighbors:
                new_value = self.alphabeta_undirected(neighbor, alpha, beta, False)
                value = max(value, new_value)
                alpha = max(alpha, value)
                if alpha >= beta:
                    break

            return value
        else:
            value = float('inf')
            neighbors = self.graph[current_vertex]

            for neighbor in neighbors:
                new_value = self.alphabeta_undirected(neighbor, alpha, beta, True)
                value = min(value, new_value)
                beta = min(beta, value)
                if alpha >= beta:
                    break

            return value

    def alphabeta_directed(self, current_vertex, alpha, beta, is_max_player):
        if current_vertex in goal_node:
            return current_vertex

        if is_max_player:
            value = float('-inf')
            neighbors = self.graph[current_vertex]

            for neighbor in neighbors:
                new_value = self.alphabeta_directed(neighbor, alpha, beta, False)
                value = max(value, new_value)
                alpha = max(alpha, value)
                if alpha >= beta:
                    break

            return value
        else:
            value = float('inf')
            neighbors = self.graph[current_vertex]

            for neighbor in neighbors:
                new_value = self.alphabeta_directed(neighbor, alpha, beta, True)
                value = min(value, new_value)
                beta = min(beta, value)
                if alpha >= beta:
                    break

            return value
