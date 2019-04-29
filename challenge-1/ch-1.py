import math
import os

in_file_path = os.path.join(os.path.dirname(__file__), "submitInput")
out_file_path = os.path.join(os.path.dirname(__file__), "submitOutput.txt")

with open(in_file_path, 'r') as infile:
    with open(out_file_path, 'w') as outfile:
        cases = int(infile.readline())

        for case in range(cases):
            lines = list(map(int, (infile.readline().split())))
            onion = lines[0]
            nonion = lines[1]

            total = math.ceil(onion / 2) + math.ceil(nonion / 2)

            print(onion, nonion, total)

            outfile.write("Case #" + str(case + 1) + ": " + str(total) + "\n")
