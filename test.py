import timeit


def filter_comparison():
    first = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3]
    second = [1, 4, 5, 8, 7, 4, 3]

    return set(filter(lambda x: x not in second, first))


def comprehension_comparison():
    first = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3]
    second = [1, 4, 5, 8, 7, 4, 3]

    return set([x for x in first if x not in second])


def remove_zeros():
    arr = [0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4, 0]

    x = 0  # the only one variable
    while x < len(arr):
        if not arr[x]:
            arr.remove(arr[x])
            continue
        x += 1

    return arr


def run():
    print(filter_comparison())
    print(timeit.timeit(filter_comparison, number=1000))

    print(comprehension_comparison())
    print(timeit.timeit(comprehension_comparison, number=1000))

    print(remove_zeros())
