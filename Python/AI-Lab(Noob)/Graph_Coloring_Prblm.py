def is_safe(v,graph, color, c):


# backtracking function to solve graph coloring problem
def graph_coloring_util(graph, m, color, v):





# Main driver function 
def graph_coloring(graph, m):



# Driver Code
if __name__ == "__main__":
    # Create a graph given in the above diagram
    graph = [[0, 1, 1, 1],
             [1, 0, 1, 0],
             [1, 1, 0, 1],
             [1, 0, 1, 0]]
    m = 3
    graph_coloring(graph, m)
    