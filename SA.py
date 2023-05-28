import random
import math


class Graph_SimulatedAnnealing:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType = graphType

    def print_path(self, tracepath):
        for t in tracepath:
            print(t, end=" ")
        print()  # Add a newline after printing the path

    def simulated_annealing(self, start_node, goal_node, temperature, cooling_rate):
        if self.graphType == "Undirected Graph":
            return self.simulated_annealing_undirected(start_node, goal_node, temperature, cooling_rate)
        else:
            return self.simulated_annealing_directed(start_node, goal_node, temperature, cooling_rate)

    def simulated_annealing_undirected(self, current_node, goal_node, temperature, cooling_rate):
        current_solution = [current_node]
        current_cost = self.calculate_cost(current_solution, goal_node)

        while temperature > 0.1:
            neighbor = self.get_random_neighbor(current_solution)
            neighbor_cost = self.calculate_cost(neighbor, goal_node)
            cost_difference = neighbor_cost - current_cost

            if cost_difference < 0 or math.exp(-cost_difference / temperature) > random.random():
                current_solution = neighbor
                current_cost = neighbor_cost

            temperature *= cooling_rate

        return current_solution

    def simulated_annealing_directed(self, current_node, goal_node, temperature, cooling_rate):
        current_solution = [current_node]
        current_cost = self.calculate_cost(current_solution, goal_node)

        while temperature > 0.1:
            neighbor = self.get_random_neighbor(current_solution)
            neighbor_cost = self.calculate_cost(neighbor, goal_node)
            cost_difference = neighbor_cost - current_cost

            if cost_difference < 0 or math.exp(-cost_difference / temperature) > random.random():
                current_solution = neighbor
                current_cost = neighbor_cost

            temperature *= cooling_rate

        return current_solution

    def get_random_neighbor(self, solution):
        random_node = random.choice(solution)
        neighbors = self.graph[random_node]
        neighbor = random.choice(neighbors)
        neighbor_solution = solution[:]
        neighbor_solution.append(neighbor)
        return neighbor_solution

    def calculate_cost(self, solution, goal_node):
        last_node = solution[-1]
        return len(solution) + self.heuristic(last_node, goal_node)

    def heuristic(self, current_node, goal_node):
        return abs(goal_node - current_node)
