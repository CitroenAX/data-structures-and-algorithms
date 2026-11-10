# jumps.py


def jumps(n, a, b):
    # ways_to_reach[level] stores the number of ways to reach that level.
    ways_to_reach = []
    for level in range(n + 1):
        ways_to_reach.append(0)

    # There is one way to be at the starting level: do not jump.
    ways_to_reach[0] = 1

    for level in range(1, n + 1):
        ways_from_a_levels_back = 0
        if level >= a:
            ways_from_a_levels_back = ways_to_reach[level - a]

        ways_from_b_levels_back = 0
        if level >= b:
            ways_from_b_levels_back = ways_to_reach[level - b]

        # The last jump must be either a or b levels long.
        ways_to_reach[level] = (
            ways_from_a_levels_back + ways_from_b_levels_back
        )

    return ways_to_reach[n]


if __name__ == "__main__":
    print(jumps(4, 1, 2))
    print(jumps(8, 2, 3))
    print(jumps(11, 6, 7))
    print(jumps(30, 3, 5))
    print(jumps(100, 4, 5))