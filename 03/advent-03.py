import string

ITEM_PRIORITIES = {x: i + 1 for i, x in enumerate(string.ascii_letters)}


def open_rucksacks(filename: str):
    with open(filename, "r") as f:
        sacks = ((clean := x.strip(), len(clean) // 2) for x in f.readlines())
    return [(set(x[:y]), set(x[y:])) for x, y in sacks]


def find_common_priority(comp1: str, comp2: str):
    common = comp1 & comp2
    return (ITEM_PRIORITIES[x] for x in common)


def find_badge_priority(sack1: tuple[str], sack2: tuple[str], sack3: tuple[str]):
    badge_items = (sack1[0] | sack1[1]) & (sack2[0] | sack2[1]) & (sack3[0] | sack3[1])
    return (ITEM_PRIORITIES[x] for x in badge_items)


if __name__ == "__main__":
    rucksacks = open_rucksacks("input.txt")
    # part one
    total = 0
    for sack in rucksacks:
        for item in find_common_priority(*sack):
            total += item
    print(f"Part One: {total}")
    # part two
    total = 0
    for n in range(0,len(rucksacks),3):
        for item in find_badge_priority(rucksacks[n], rucksacks[n+1], rucksacks[n+2]):
            total += item
    print(f"Part Two: {total}")
