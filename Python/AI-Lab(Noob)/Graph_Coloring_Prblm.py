def is_safe(v,graph, color, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

# backtracking function to solve graph coloring problem
def graph_coloring_util(graph, m, color, v):
    if v == len(graph):
        print_solution(color)
        return True

    for c in range(1, m + 1):
        if is_safe(v, graph, color, c):
            color[v] = c
            if graph_coloring_util(graph, m, color, v + 1):
                return True
            color[v] = 0

    return False


def print_solution(color):
    print("Solution Exists: Following are the assigned colors:")
    for c in color:
        print(c, end=' ')
    print()


def graph_coloring(graph, m):
    color = [0] * len(graph)
    if not graph_coloring_util(graph, m, color, 0):
        print("Solution does not exist")
        return False
    return True


# Driver Code
if __name__ == "__main__":
    # Create a graph given in the above diagram
    graph = [[0, 1, 1, 1],
             [1, 0, 1, 0],
             [1, 1, 0, 1],
             [1, 0, 1, 0]]
    m = 3
    graph_coloring(graph, m)
