import os

import networkx as nx

in_file_path = os.path.join(os.path.dirname(__file__), "submitInput")
out_file_path = os.path.join(os.path.dirname(__file__), "submitOutput.txt")


def count_graph_paths(graph):
    list_paths = []
    for path in nx.all_simple_paths(graph, source='Galactica', target='New Earth'):
        list_paths.append(path)
    return len(list_paths)


def graph_from_dict(graph_dict):
    g = nx.DiGraph()
    # Create the nodes from the dictionary keys
    g.add_nodes_from(graph_dict.keys())
    # Loop through the dictionary items to create the edges between nodes
    for k, v in graph_dict.items():
        g.add_edges_from([(k, t) for t in v])
    return g


with open(in_file_path, 'r') as infile:
    with open(out_file_path, 'w') as outfile:
        cases = int(infile.readline())

        for case in range(cases):
            planets = int(infile.readline())
            graph = {}

            for i in range(planets):
                route = infile.readline().split(':')
                origin = route[0]
                destinations = route[1].rstrip().split(',')
                graph[origin] = destinations
                stellar_map = graph_from_dict(graph)

            num_paths = count_graph_paths(stellar_map)
            outfile.write("Case #" + str(case + 1) + ": " + str(num_paths) + "\n")
