def count(in_: [int]) -> int:
    previous = None
    count = 0
    for i in in_:
        if previous is not None and previous < i:
            count += 1
        previous = i
    return count


if __name__ == "__main__":
    print(count([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]))
    with open("input", "r") as f:
        lines = f.readlines()
    values = [int(line) for line in lines]
    print(count(values))

