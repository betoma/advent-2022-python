def count_calories(content):
    elves = []
    n = 0
    for line in content:
        li = line.strip()
        if li:
            n += int(li)
        else:
            elves.append(n)
            n = 0
    return elves

def main():
    with open("input.txt", "r") as f:
        elf_list = count_calories(f.readlines())
    elf_list.sort(reverse=True)
    # part one
    print(elf_list[0])
    # part two
    print(sum(elf_list[:3]))

if __name__ == "__main__":
    main()

