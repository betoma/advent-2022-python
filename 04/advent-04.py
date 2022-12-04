def load_assignments(filename: str):
    with open(filename, "r") as f:
        assignments = [
            tuple([tuple(map(int, y.split("-"))) for y in x.strip().split(",")])
            for x in f.readlines()
        ]
    return assignments


def pairs_contain_each_other(assignments: list[tuple[tuple]]):
    duplicates = []
    for pair in assignments:
        if (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or (
            pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]
        ):
            duplicates.append(pair)
    return duplicates


def pairs_overlap(assignments: list[tuple[tuple]]):
    overlaps = []
    for pair in assignments:
        if (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][0]) or (
            pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][0]
        ):
            overlaps.append(pair)
    return overlaps


if __name__ == "__main__":
    pairs = load_assignments("input.txt")
    # part one
    print(len(pairs_contain_each_other(pairs)))
    # part two
    print(len(pairs_overlap(pairs)))
