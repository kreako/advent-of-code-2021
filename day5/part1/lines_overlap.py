from collections import defaultdict


class Diagram(object):

    def __init__(self):
        self.points = defaultdict(int)

    def add_line(self, x1, y1, x2, y2):
        if x1 == x2:
            x = x1
            for y in range(min(y1, y2), max(y1, y2) + 1):
                self.points[(x, y)] += 1
        elif y1 == y2:
            y = y1
            for x in range(min(x1, x2), max(x1, x2) + 1):
                self.points[(x, y)] += 1
        else:
            pass
            # raise Exception(f"Invalid line {x1} {y1} {x2} {y2}")

    def count_overlap(self):
        count = 0
        overlap_points = list(filter(lambda x: x > 1, self.points.values()))
        return len(overlap_points)


def parse_line(line):
    x1y1, x2y2 = line.strip().split(" -> ")
    x1, y1 = [int(e) for e in x1y1.split(",")]
    x2, y2 = [int(e) for e in x2y2.split(",")]
    return (x1, y1, x2, y2)


if __name__ == "__main__":
    little = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""
    diagram = Diagram()
    for line in little.splitlines():
        diagram.add_line(*parse_line(line))
    print(diagram.count_overlap())

    diagram = Diagram()
    with open("../input", "r") as f:
        for line in f:
            diagram.add_line(*parse_line(line))
    print(diagram.count_overlap())
