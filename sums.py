# sums.py


def sums(items):
    # can_make_sum[total] is True if some items can make that total.
    maximum_sum = 0
    for item in items:
        maximum_sum += item

    # Create one entry for each possible total, from 0 to maximum_sum.
    can_make_sum = []
    for total in range(maximum_sum + 1):
        can_make_sum.append(False)

    # Choosing no items makes a total of 0.
    can_make_sum[0] = True

    for item in items:
        # Go downward so each item is used at most once.
        for total in range(maximum_sum, item - 1, -1):
            if can_make_sum[total - item]:
                can_make_sum[total] = True

    count = 0
    for total in range(1, maximum_sum + 1):
        if can_make_sum[total]:
            count += 1

    return count


if __name__ == "__main__":
    print(sums([1, 2, 3]))
    print(sums([2, 2, 3]))
    print(sums([1, 3, 5, 1, 3, 5]))
    print(sums([1, 15, 5, 23, 100, 55, 2]))