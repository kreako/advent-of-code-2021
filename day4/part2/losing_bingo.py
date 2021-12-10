class Board(object):

    def __init__(self, boards):
        if len(boards) != 25:
            raise Exception(f"Invalid board : {len(boards)}")
        self.boards = boards
        self.marked = [False] * 25
        self.won = False

    @staticmethod
    def parse(lines):
        boards = []
        for line in lines:
            boards.extend([int(x) for x in line.split()])
        return Board(boards)

    def mark(self, nb):
        for i, n in enumerate(self.boards):
            if n == nb:
                self.marked[i] = True

    def check_won(self):
        # row
        for i in range(0, 25, 5):
            if all(self.marked[i: i + 5]):
                self.won = True
        # col
        for i in range(5):
            if all(self.marked[i::5]):
                self.won = True

    def unmarked(self):
        u = []
        for i, m in enumerate(self.marked):
            if not m:
                u.append(self.boards[i])
        return u


class Bingo(object):

    def __init__(self, order, boards):
        self.order = order
        self.boards = boards

    @staticmethod
    def parse(text: str):
        lines = text.splitlines()
        order = [int(x) for x in lines[0].split(",")]
        boards = []
        l = 2
        while True:
            boards.append(Board.parse(lines[l: l + 5]))
            l += 6
            if l >= len(lines):
                break
        return Bingo(order, boards)

    def play(self):
        for o in self.order:
            boards = list(filter(lambda x: x.won == False, self.boards))
            for board in boards:
                board.mark(o)
                board.check_won()
                if len(boards) == 1 and board.won:
                    return sum(board.unmarked()) * o


if __name__ == "__main__":
    little = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
  """

    bingo = Bingo.parse(little)
    print(bingo.play())

    with open("../input", "r") as f:
        bingo = Bingo.parse(f.read())

    print(bingo.play())
