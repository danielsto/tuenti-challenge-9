import math
import os

in_file_path = os.path.join(os.path.dirname(__file__), "testInput")
out_file_path = os.path.join(os.path.dirname(__file__), "testOutput.txt")

with open(in_file_path, 'r') as infile:
    with open(out_file_path, 'w') as outfile:
        cases = int(infile.readline())

        for case in range(cases):
            planets = int(infile.readline())
            print(planets)
            graph = {}
            for i in range(planets):
                route = infile.readline().split(':')
                origin = route[0]
                destinations = route[1].rstrip().split(',')
                graph[origin] = destinations
                print(graph)

            #outfile.write("Case #" + str(case + 1) + ": " + str(total) + "\n")