
def quick_sort(l):
    if len(l) < 2:
        return l
    pivot = l[-1]
    smaller = []
    bigger = []
    for n in l[:-1]:
        if pivot > n:
            smaller.append(n)
        else:
            bigger.append(n)
    left = quick_sort(smaller)
    right = quick_sort(bigger)
    print('left: {}'.format(left))
    print('right: {}'.format(right))
    print('pivot: {}'.format(pivot))
    print(left + [pivot] + right)
    return left + [pivot] + right


if __name__ == '__main__':
    input_list = [5, 9, 3, 1, 2, 8, 4, 7, 6]

    sorted_list = quick_sort(input_list)

    assert sorted_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]

