import os

in_file_path = os.path.join(os.path.dirname(__file__), "testInput")
out_file_path = os.path.join(os.path.dirname(__file__), "testOutput.txt")


def TopologicalSort(graph):
    TopologicalSortedList = []  # result
    ZeroInDegreeVertexList = []  # node with 0 in-degree/inbound neighbours
    inDegree = {u: 0 for u in graph}  # inDegree/inbound neighbours

    # Step 1: Iterate graph and build in-degree for each node
    for u in graph:
        for v in graph[u]:
            inDegree[v] += 1

    # Step 2: Find node(s) with 0 in-degree
    for k in inDegree:
        # print("##########", k,inDegree[k])
        if (inDegree[k] == 0):
            ZeroInDegreeVertexList.append(k)

            # Step 3: Process nodes with in-degree = 0
    while ZeroInDegreeVertexList:
        v = ZeroInDegreeVertexList.pop(0)  # order in important!
        TopologicalSortedList.append(v)
        # Step 4: Update in-degree
        for neighbour in graph[v]:
            inDegree[neighbour] -= 1
            if (inDegree[neighbour] == 0):
                ZeroInDegreeVertexList.append(neighbour)

    return TopologicalSortedList


def build_graph(a):
    # a = ['u', 'uud', 'udu', 'd', 'du', 'duu', 'ddu']
    # a = ['mm', 'mmng', 'mtgt', 'nnntng', 'ng', 'tn', 'tgt', 'g', 'gg', 'ggg']
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
        word2 = a[i+1]

        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                print(graph)
                # print(word1[j], word2[j],  word1[j] not in graph[word2[j]])
                if len(graph[word1[j]]) == 0 and  word1[j] not in graph[word2[j]]:
                    graph[word1[j]].append(word2[j])
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
            graph = build_graph(alphabet)

            order = TopologicalSort(graph)

            if len(order) > 0:
                order = " ".join(TopologicalSort(graph))
            else:
                order = "AMBIGUOUS"

            outfile.write("Case #" + str(case + 1) + ": " + order + "\n")
