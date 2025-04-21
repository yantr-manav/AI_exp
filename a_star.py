import heapq


class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name
        self.parent = parent
        # Cost from start to current node
        self.g = g
        # Heuristic estimate to goal
        self.h = h
        # Total cost
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f


def a_star_search(graph, heuristics, start, goal):
    open_list = []
    closed_list = set()

    start_node = Node(start, None, 0, heuristics[start])
    heapq.heappush(open_list, start_node)

    while open_list:
        # Get node with lowest f(n)
        current_node = heapq.heappop(open_list)

        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]

        closed_list.add(current_node.name)

        for neighbor, cost in graph[current_node.name].items():
            if neighbor in closed_list:
                continue

            g = current_node.g + cost
            h = heuristics[neighbor]
            new_node = Node(neighbor, current_node, g, h)

            if not any(n.name == new_node.name and n.f <= new_node.f for n in open_list):
                heapq.heappush(open_list, new_node)

    return None


graph = {
    'A': {'B': 1, 'D': 3},
    'B': {'A': 1, 'C': 1, 'F': 4, 'E': 2},
    'C': {'B': 1, 'G': 2},
    'D': {'A': 3, 'F': 2},
    'E': {'B': 2, 'G': 3},
    'F': {'B': 4, 'D': 2, 'E': 3},
    'G': {'C': 2, 'E': 3}
}


# Heuristic Values (Estimated cost to reach 'G')
heuristics = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'F': 3,
    'G': 0
}


# A* Search
start_node = 'A'
goal_node = 'G'
path = a_star_search(graph, heuristics, start_node, goal_node)


print(f"Path from {start_node} to {goal_node}: {path}")
