from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    traversal = []

    while queue:
        vertex = queue.popleft()
        traversal.append(vertex)

        # Visit all unvisited neighbors
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal


def input_graph():
    graph = {}
    n = int(input("Enter the number of nodes: "))
    for _ in range(n):
        node = input("Enter node label: ")
        node = node.strip()
        neighbors = input(
            f"Enter neighbors of {node} (space-separated): ").split()
        graph[node] = neighbors
    return graph


def main():
    print("Input Graph")
    graph = input_graph()
    start_node = input("Enter the starting node for BFS: ")

    print("\nBFS Traversal:")
    traversal = bfs(graph, start_node)
    print(" -> ".join(traversal))


if __name__ == "__main__":
    main()
