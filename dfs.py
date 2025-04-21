def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    visited.add(start)

    traversal = []

    while stack:
        vertex = stack.pop()
        traversal.append(vertex)

        # Adding all unvisited neighbors to the stack
        # reversed to match recursive DFS order
        for neighbor in reversed(graph[vertex]):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return traversal


def input_graph():
    graph = {}
    n = int(input("Enter the number of nodes: "))
    for _ in range(n):
        node = input("Enter node label: ")
        neighbors = input(
            f"Enter neighbors of {node} (space-separated): ").split()
        graph[node] = neighbors
    return graph


def main():
    print("Input Graph")
    graph = input_graph()
    start_node = input("Enter the starting node for DFS: ")

    print("\nDFS Traversal:")
    traversal = dfs_iterative(graph, start_node)
    print(" -> ".join(traversal))


if __name__ == "__main__":
    main()
