def count(lines, position):
    c = {1: 0, 0: 0}
    for l in lines:
        s = l[position]
        c[int(s)] += 1
    return c


def lines_filter(lines, position, selector):
    c = count(lines, position)
    digit = str(selector(c))
    return list(filter(lambda x: x[position] == digit, lines))


def lines_reduce(lines, selector):
    position = 0
    while len(lines) > 1:
        lines = lines_filter(lines, position, selector)
        position += 1
    return lines[0]


def compute(lines):
    def most_common(c):
        if c[1] >= c[0]:
            return 1
        return 0

    def least_common(c):
        if c[0] <= c[1]:
            return 0
        return 1

    oxygen = int(lines_reduce(lines, most_common), 2)
    co2 = int(lines_reduce(lines, least_common), 2)

    print(oxygen, co2, oxygen * co2)


if __name__ == "__main__":
    little = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    print(count(little, 0))
    print(count(little, 1))
    print(count(little, 2))
    print(count(little, 3))
    print(count(little, 4))

    compute(little)

    with open("../input", "r") as f:
        compute(f.readlines())
