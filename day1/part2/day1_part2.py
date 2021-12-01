def count(in_: [int]) -> int:
    previous = sum(in_[0:3])
    count = 0
    for i in range(len(in_) - 3 + 1):
        s = sum(in_[i: i + 3])
        if previous < s:
            count += 1
        previous = s
    return count


if __name__ == "__main__":
    print(count([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]))
    with open("input", "r") as f:
        lines = f.readlines()
    values = [int(line) for line in lines]
    print(count(values))

