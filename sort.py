
def selection_sort(l):
    length = len(l)
    for i in range(length - 1, -1, -1):  # TODO Hard to understand
        idx_min = length - 1 - i
        for j in range(length - i, length):
            if l[idx_min] > l[j]:
                idx_min = j
        min_val = l[idx_min]
        l[idx_min] = l[length - i - 1]
        l[length - i - 1] = min_val
        print('min: %d' % min_val)
        print(l)
    return l



def bubble_sort(l):
    length = len(l)
    for i in range(length - 1, -1, -1):  # TODO Hard to understand
        for j in range(length - 1, length - i - 1 , -1):
            # print(l[j], l[j - 1])
            print(l)
            if l[j - 1] > l[j]:
                tmp = l[j]
                l[j] = l[j - 1]
                l[j - 1] = tmp
        print('round done')
    return l


if __name__ == '__main__':
    input_list = [5, 9, 3, 1, 2, 8, 4, 7, 6]

    # sorted_list = bubble_sort(input_list)
    sorted_list = selection_sort(input_list)

    assert sorted_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]
