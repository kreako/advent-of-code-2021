import math
import random


SIZE = 100


def display_tirage():
    positions = [0] * SIZE
    for tirage in range(10000):
        position = int(SIZE / 2)
        # print(position)
        for i in range(1000):
            positions[position] += 1
            if position == 0:
                position = 1
            elif position == SIZE - 1:
                position = SIZE - 2
            else:
                if random.randint(0, 1) == 0:
                    position -= 1
                else:
                    position += 1
    # Now display positions
    count_max = max(positions)
    # normalize
    normed = [20 * x / count_max for x in positions]
    for line in range(20, 0, -1):
        p = ["#"]
        for n in normed:
            if n >= line:
                p.append('*')
            else:
                p.append(' ')
        p.append("#")
        print("".join(p))

    # print(count_max)
    # print(positions)


def move_rabbit(rabbit):
    if rabbit == 0:
        return 1
    elif rabbit == SIZE - 1:
        return SIZE - 2
    else:
        if random.randint(0, 1) == 0:
            return rabbit - 1
        else:
            return rabbit + 1


def chasing_rabbit_fix():
    rabbit = random.randint(0, SIZE - 1)
    count = 0
    me = int(SIZE / 2)
    while True:
        if me == rabbit:
            return count
        rabbit = move_rabbit(rabbit)
        count += 1


def chasing_rabbit_running_even():
    rabbit = random.randint(0, SIZE - 1)
    count = 0
    me = 0
    while True:
        # print(rabbit, me)
        if me == rabbit:
            return count
        rabbit = move_rabbit(rabbit)
        me += 2
        if me >= SIZE:
            me = 0
        count += 1


def chasing_rabbit_running_step():
    rabbit = random.randint(0, SIZE - 1)
    count = 0
    me = 0
    step = 0
    while True:
        # print(rabbit, me)
        if me == rabbit:
            return count
        rabbit = move_rabbit(rabbit)
        if step == 1:
            me += 2
            step = 0
        else:
            step = 1
        if me >= SIZE:
            me = 0
        count += 1


def chasing_rabbit_running_even_odd():
    rabbit = random.randint(0, SIZE - 1)
    count = 0
    me = 0
    while True:
        # print(rabbit, me)
        if me == rabbit:
            return count
        rabbit = move_rabbit(rabbit)
        me += 2
        if me >= SIZE:
            if me % 2 == 0:
                me = 1
            else:
                me = 0
        count += 1


def average(f, length):
    count_sum = 0
    count_min = math.inf
    count_max = -math.inf
    for i in range(length):
        count = f()
        count_min = min(count, count_min)
        count_max = max(count, count_max)
        count_sum += count
        # print(i, count, count_min, count_max, count_sum)
    print(f.__name__)
    print("min", count_min)
    print("max", count_max)
    print("avg", count_sum/length)


if __name__ == "__main__":
    average(chasing_rabbit_running_even_odd, 1000000)
    average(chasing_rabbit_running_even, 1000000)
    # average(chasing_rabbit_fix, 1000)
