# jumps.py


def jumps(n, a, b):
    ways = [0] * (n + 1)
    ways[0] = 1

    for level in range(1, n + 1):
        if level >= a:
            ways[level] += ways[level - a]
        if level >= b:
            ways[level] += ways[level - b]

    return ways[n]


if __name__ == "__main__":
    print(jumps(4, 1, 2))
    print(jumps(8, 2, 3))
    print(jumps(11, 6, 7))
    print(jumps(30, 3, 5))
    print(jumps(100, 4, 5))