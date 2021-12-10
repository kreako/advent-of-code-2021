class SubMarine(object):

    def __init__(self):
        self.horizontal_position = 0
        self.depth = 0
        self.aim = 0

    def forward(self, n):
        self.horizontal_position += n
        self.depth += self.aim * n

    def up(self, n):
        self.aim -= n

    def down(self, n):
        self.aim += n


def move(lines):
    sub = SubMarine()

    for line in lines:
        movement, qtity = line.split()
        qtity = int(qtity)
        if movement == "forward":
            sub.forward(qtity)
        elif movement == "up":
            sub.up(qtity)
        elif movement == "down":
            sub.down(qtity)
        else:
            raise Exception(f"Invalid movement: {movement}")

    return sub.horizontal_position * sub.depth


if __name__ == "__main__":
    r = move(["forward 5",
              "down 5",
              "forward 8",
              "up 3",
              "down 8",
              "forward 2", ])
    print(r)
    with open("input", "r") as f:
        r = move(f.readlines())
    print(r)
