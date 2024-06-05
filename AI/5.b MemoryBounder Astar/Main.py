import heapq

def heuristic(n):
    H_dist = {
        'A': 11, 'B': 6, 'C': 5, 'D': 7, 'E': 3,
        'F': 6, 'G': 5, 'H': 3, 'I': 1, 'J': 0
    }
    return H_dist[n]

def get_neighbors(node):
    if node in Graph_nodes:
        return Graph_nodes[node]
    else:
        return []

def memory_bounded_a_star(start_node, stop_node, memory_limit):
    open_set = []
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}

    # f-cost is g(n) + heuristic(n)
    f_cost = {start_node: g[start_node] + heuristic(start_node)}

    heapq.heappush(open_set, (f_cost[start_node], start_node))

    while open_set:
        _, n = heapq.heappop(open_set)

        if n == stop_node or n not in Graph_nodes:
            break

        closed_set.add(n)

        for (m, weight) in get_neighbors(n):
            if m not in closed_set:
                new_g = g[n] + weight

                if m not in g or new_g < g[m]:
                    g[m] = new_g
                    parents[m] = n
                    f_cost[m] = g[m] + heuristic(m)

                    if f_cost[m] <= memory_limit:
                        heapq.heappush(open_set, (f_cost[m], m))

    if n == stop_node:
        path = []
        while parents[n] != n:
            path.append(n)
            n = parents[n]
        path.append(start_node)
        path.reverse()
        print('Path found: {}'.format(path))
        return path
    else:
        print('Path does not exist within the memory limit.')
        return None

# Rest of the code remains the same as the A* algorithm example

Graph_nodes = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
}

memory_bounded_a_star('A', 'J', memory_limit=20)