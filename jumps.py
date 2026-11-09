"""Count paths to level n using jumps of size a or b."""


def jumps(n: int, a: int, b: int) -> int:
    """Return the number of ways to reach level n.

    Let ways[level] count paths to that level. The last jump must be either
    a or b levels, so ways[level] = ways[level - a] + ways[level - b],
    ignoring terms whose indices are negative. Each level is computed once,
    giving Theta(n) time and O(n) space.
    """
    ways = [0] * (n + 1)
    ways[0] = 1

    for level in range(1, n + 1):
        if level >= a:
            ways[level] += ways[level - a]
        if level >= b:
            ways[level] += ways[level - b]

    return ways[n]


if __name__ == "__main__":
    print(jumps(8, 2, 3))  # 4