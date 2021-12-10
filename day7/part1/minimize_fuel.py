def median(l):
    l.sort()
    return l[len(l)//2]


def sum_diff_median(l, m):
    return sum([abs(x - m) for x in l])


if __name__ == "__main__":
    little = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    m = median(little)
    print(sum_diff_median(little, m))

    with open("../input", "r") as f:
        l = [int(x) for x in f.read().split(",")]
    m = median(l)
    print(sum_diff_median(l, m))
