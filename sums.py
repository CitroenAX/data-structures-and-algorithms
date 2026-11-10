# sums.py


def sums(items):
    maximum_sum = 0
    for item in items:
        maximum_sum += item

    # possible_sums[i][total] tells whether total can be made
    # using only the first i items.
    possible_sums = []
    for item_count in range(len(items) + 1):
        row = []
        for total in range(maximum_sum + 1):
            row.append(False)
        possible_sums.append(row)

    # Using no items, only a total of 0 is possible.
    possible_sums[0][0] = True

    for item_count in range(1, len(items) + 1):
        item = items[item_count - 1]

        for total in range(maximum_sum + 1):
            # First, try making this total without the current item.
            possible_sums[item_count][total] = possible_sums[item_count - 1][total]

            # Then, try making it with the current item.
            if total >= item:
                if possible_sums[item_count - 1][total - item]:
                    possible_sums[item_count][total] = True

    count = 0
    for total in range(1, maximum_sum + 1):
        if possible_sums[len(items)][total]:
            count += 1

    return count


if __name__ == "__main__":
    print(sums([1, 2, 3]))
    print(sums([2, 2, 3]))
    print(sums([1, 3, 5, 1, 3, 5]))
    print(sums([1, 15, 5, 23, 100, 55, 2]))