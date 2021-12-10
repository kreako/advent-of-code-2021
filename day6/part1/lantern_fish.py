from collections import defaultdict


class Fishes(object):

    def __init__(self, ages):
        self.ages = defaultdict(int)
        for age in ages:
            self.ages[age] += 1

    def next_generation(self):
        new_born = self.ages[0]
        for i in range(8):
            self.ages[i] = self.ages[i + 1]
        self.ages[6] += new_born
        self.ages[8] = new_born

    def count(self):
        return sum(self.ages.values())


if __name__ == "__main__":
    little = "3,4,3,1,2"
    fishes = Fishes([int(a) for a in little.split(",")])
    for _ in range(80):
        fishes.next_generation()
    print(fishes.count())

    with open("../input", "r") as f:
        fishes = Fishes([int(a) for a in f.read().split(",")])
    for i in range(80):
        fishes.next_generation()
    print(fishes.count())
