import fractions
import os

import numpy as np

in_file_path = os.path.join(os.path.dirname(__file__), "submitInput")
out_file_path = os.path.join(os.path.dirname(__file__), "submitOutput.txt")


def get_original_list(entries):
    # Halla una lista con el mínimo común múltiplo de todos
    highest = max(entries)
    occurrences = entries.count(highest)
    repeat = highest
    if occurrences < highest:
        for el in entries:
            while repeat % el != 0 and el != highest:
                repeat += highest

        new_entries = list(np.repeat(entries, repeat))
    else:
        return entries
    return new_entries


def get_count_candies(entries):
    # How many people [value] want how many candies [key]
    counts = {}
    for element in list(set(entries)):
        counts[element] = entries.count(element)
    # print(counts)
    return counts


def get_people_and_candies(count_dict):
    # Loop through the dict and multiply key by value to know how much candy there is needed
    # Key/Value to know how much people there are
    people = 0
    candy = 0
    for key in count_dict:
        people += count_dict[key] / key
        candy += float(count_dict[key])
    return people, candy


with open(in_file_path, 'r') as infile:
    with open(out_file_path, 'w') as outfile:
        cases = int(infile.readline())

        for case in range(cases):
            num_entries = int(infile.readline())
            entries = list(map(int, (infile.readline().split())))

            entries = get_original_list(entries)
            num_candies = get_count_candies(entries)
            people, candy = get_people_and_candies(num_candies)
            average_candy = fractions.Fraction(candy / people).limit_denominator()
            outfile.write("Case #" + str(case + 1) + ": " + str(average_candy) + "\n")
