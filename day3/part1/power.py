from collections import defaultdict


class Counter(object):

    def __init__(self):
        # count : index -> {1: <count of 1>, 0: <count of 0>}
        def default_factory():
            return {1: 0, 0: 0}
        self._count = defaultdict(default_factory)

    def count(self, line):
        for i, s in enumerate(reversed(line)):
            digit = int(s)
            self._count[i][digit] += 1

    def most_common(self):
        nb = 0
        for i in self._count.keys():
            if self._count[i][1] > self._count[i][0]:
                # set bit to 1 on position i
                nb = nb | (1 << i)
        return nb

    def least_common(self):
        nb = 0
        for i in self._count.keys():
            if self._count[i][1] < self._count[i][0]:
                # set bit to 1 on position i
                nb = nb | (1 << i)
        return nb


def count(lines):
    counter = Counter()
    for line in lines:
        counter.count(line.strip())
    print(bin(counter.most_common()), bin(counter.least_common()),
          counter.most_common() * counter.least_common())


if __name__ == "__main__":
    count([
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
    ])

    with open("../input", "r") as f:
        count(f.readlines())
