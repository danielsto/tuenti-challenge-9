import os

in_file_path = os.path.join(os.path.dirname(__file__), "submitInput")
out_file_path = os.path.join(os.path.dirname(__file__), "submitOutput.txt")

# typewriter = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
#              'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
#              'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';',
#              'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '-']

typewriter = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
              ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
              ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';'],
              ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '-']]


def get_special_displacement(sender, encripted):
    for line in typewriter:
        if sender in line:
            sender_line = line
        elif encripted in line:
            encripted_line = line
        else:
            continue
    row_displacement = typewriter.index(sender_line) - typewriter.index(encripted_line)
    column_displacement = sender_line.index(sender) - encripted_line.index(encripted)
    displacement = [row_displacement, column_displacement]
    return displacement


def get_displacement(sender, encripted):
    for line in typewriter:
        if sender in line and encripted in line:
            displacement = line.index(sender) - line.index(encripted)
            return displacement
        else:
            continue
    displacement = get_special_displacement(sender, encripted)
    return displacement


def decode(encripted, displacement):
    for line in typewriter:
        if encripted in line:
            encripted_line = line
            if type(displacement) == list:
                # Cuando el desplazamiento es en distintas líneas y columnas
                # TODO: contemplar cuando se salta el rango
                decoded_line_index = (typewriter.index(encripted_line) + displacement[0])
                if decoded_line_index >= len(typewriter):
                    decoded_line_index -= len(typewriter)
                elif decoded_line_index < 0:
                    decoded_line_index += len(typewriter)
                #print("DECODED LINE INDEX:", decoded_line_index)
                decoded_line = typewriter[decoded_line_index]
                #print("DECODED LINE:", decoded_line)
                decoded_col_index = encripted_line.index(encripted) + displacement[1]
                if decoded_col_index >= len(encripted_line):
                    decoded_col_index -= len(encripted_line)
                if decoded_col_index < 0:
                    decoded_col_index += len(encripted_line)
                decoded = decoded_line[decoded_col_index]
                return decoded
            else:
                # Cuando el desplazamiento es en la misma línea
                new_index = encripted_line.index(encripted) + displacement
                if new_index >= len(encripted_line):
                    new_index -= len(encripted_line)
                elif new_index < 0:
                    new_index += len(encripted_line)
                decoded = encripted_line[new_index]
                return decoded


with open(in_file_path, 'r') as infile:
    with open(out_file_path, 'w') as outfile:
        cases = int(infile.readline())

        for case in range(cases):
            sender = infile.readline().rstrip()
            message = infile.readline().rstrip()

            # message = 'P .PFF IQOZ J'
            # message = 'J 6JZZ GKH FKK8 4'
            # displacement = typewriter.index(sender) - typewriter.index(message[-1])

            displacement = get_displacement(sender, message[-1])
            # print(sender, message[-1], displacement)

            #print(sender, message[-1], displacement, decoded)
            decoded_message = ''
            for char in message:
                if char != ' ':
                    decoded_message += (decode(char, displacement))
                else:
                    decoded_message += char
            print(str(decoded_message))
            outfile.write("Case #" + str(case + 1) + ": " + str(decoded_message) + "\n")
