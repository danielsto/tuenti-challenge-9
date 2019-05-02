import os

import networkx

in_file_path = os.path.join(os.path.dirname(__file__), "submitInput")
out_file_path = os.path.join(os.path.dirname(__file__), "submitOutput.txt")


def build_graph(a):
    # a = ['u', 'uud', 'udu', 'd', 'du', 'duu', 'ddu']
    # a = ['mm', 'mmng', 'mtgt', 'nnntng', 'ng', 'tn', 'tgt', 'g', 'gg', 'ggg']
    # a = ['tvft', 'v', 'vftf']
    graph = {}
    # Creating nodes
    for word in a:
        for char in word:
            if char not in graph.keys():
                graph[char] = []

    if len(graph) > len(a):
        return {}

    for i in range(len(a) - 1):
        word1 = a[i]
        word2 = a[i + 1]

        for j in range(min(len(word1), len(word2))):
            # print(word1, word2)
            if word1[j] != word2[j]:
                graph[word1[j]].append(word2[j])
                # print(word1[j], '<', word2[j])
                break
            # print(graph)

    return graph


with open(in_file_path, 'r') as infile:
    with open(out_file_path, 'w') as outfile:
        cases = int(infile.readline())

        for case in range(cases):
            lines = int(infile.readline().rstrip())
            alphabet = []
            for l in range(lines):
                alphabet.append(infile.readline().rstrip())

            if case in range(0, 100):
                graph = build_graph(alphabet)
                # print(alphabet)
                # print(graph)
                graph = networkx.DiGraph(graph)
                # print(graph)
                order = networkx.all_topological_sorts(graph)
                order = list(order)
                # print(order, len(order))
                if len(order) > 1:
                    order = "AMBIGUOUS"
                else:
                    if len(order[0]) < 1:
                        order = "AMBIGUOUS"
                    else:
                        order = " ".join(order[0])
                print(order)
                outfile.write("Case #" + str(case + 1) + ": " + order + "\n")
