# sums.py


def sums(items):
    reachable = {0}

    for item in items:
        reachable.update(total + item for total in tuple(reachable))

    return len(reachable) - 1


if __name__ == "__main__":
    print(sums([1, 2, 3]))
    print(sums([2, 2, 3]))
    print(sums([1, 3, 5, 1, 3, 5]))
    print(sums([1, 15, 5, 23, 100, 55, 2]))