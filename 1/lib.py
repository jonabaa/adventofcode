""" Library for solutions to advent of code, day 1. """

def load_file_to_list(file_name):
    raw_lines = None
    with open(file_name, "r") as file:
            raw_lines = file.readlines()
    if raw_lines is None:
        return None
    lines = []
    for line in raw_lines:
        lines.append(int(line[:-1]))
    return lines

