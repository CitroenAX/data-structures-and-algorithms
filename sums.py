# sums.py


def sums(items):
    # reachable[total] is True if some of the items can make that total.
    maximum_sum = 0
    for item in items:
        maximum_sum += item

    reachable = [False] * (maximum_sum + 1)
    reachable[0] = True

    for item in items:
        # Go downward so each item is used at most once.
        for total in range(maximum_sum, item - 1, -1):
            if reachable[total - item]:
                reachable[total] = True

    count = 0
    for total in range(1, maximum_sum + 1):
        if reachable[total]:
            count += 1

    return count


if __name__ == "__main__":
    print(sums([1, 2, 3]))
    print(sums([2, 2, 3]))
    print(sums([1, 3, 5, 1, 3, 5]))
    print(sums([1, 15, 5, 23, 100, 55, 2]))