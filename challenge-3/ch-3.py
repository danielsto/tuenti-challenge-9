import os

in_file_path = os.path.join(os.path.dirname(__file__), "testInput")
out_file_path = os.path.join(os.path.dirname(__file__), "testOutput.txt")


def unfold_hole(direction, coord, width, height):
    coord = list(coord)
    duplicate = []
    if direction == 'T':
        coord[1] += 1 * height
        duplicate.append(coord[0])
        duplicate.append(coord[1] - (2 * (coord[1] - height) + 1))
        duplicate = tuple(duplicate)

    elif direction == 'R':
        coord[0] += 2 * width - 1 - coord[0]
        duplicate.append(coord[0] + (2 * (coord[0] - width) + 1))
        duplicate.append(coord[1])
        duplicate = tuple(duplicate)

    return tuple(coord), width, height, duplicate


#print(unfold_hole('T', (0, 0), 4, 2))
#print(unfold_hole('T', (2, 1), 4, 2))
print(unfold_hole('R', (0, 2), 4, 4))
# print(unfold_hole('R', (0, 1), 4, 4))

with open(in_file_path, 'r') as infile:
    with open(out_file_path, 'w') as outfile:
        cases = int(infile.readline())

        for case in range(cases):
            lines = list(map(int, (infile.readline().split())))
            print(lines)
            width, height, num_folds, num_holes = lines[0], lines[1], lines[2], lines[3]

            # list of folds (T, B, L, R)
            folds = []
            for fold in range(num_folds):
                folds.append(infile.readline().rstrip())

            print(folds)

            # list of tuples containing x,y coordinates of the holes
            holes = []
            for hole in range(num_holes):
                holes.append(tuple(infile.readline().rstrip().split(' ')))

            #for f in folds:
             #   for i, h in enumerate(holes):
            #        coord, width, height = unfold_hole(f, h, width, height)

            print(holes)

            break
            # outfile.write("Case #" + str(case + 1) + ": " + str(num_paths) + "\n")
