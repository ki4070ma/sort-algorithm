
# Find maximum
def selection_sort_LTR(l):
    length = len(l)
    for i in range(0, length-1):  # TODO Hard to understand around idx
        print('round start')
        idx_max = 0
        for j in range(1, length-i):
            if l[idx_max] < l[j]:
                idx_max = j
        max_val = l[idx_max]
        l[idx_max] = l[-1-i]
        l[-1-i] = max_val
        print('max: %d' % max_val)
        print(l)
    return l


# Find minimum
def selection_sort_RTL(l):
    length = len(l)
    for i in range(length-1, -1, -1):  # TODO Hard to understand around idx
        idx_min = length-1-i
        for j in range(length-i, length):
            if l[idx_min] > l[j]:
                idx_min = j
        min_val = l[idx_min]
        l[idx_min] = l[length-i-1]
        l[length-i-1] = min_val
        print('min: %d' % min_val)
        print(l)
    return l

# Right to Left, find minimum
def bubble_sort_RTL(l):
    length = len(l)
    for i in range(length-1, -1, -1):  # TODO Hard to understand around idx
        for j in range(length-1, length-i-1, -1):
            # print(l[j], l[j - 1])
            print(l)
            if l[j-1] > l[j]:
                tmp = l[j]
                l[j] = l[j-1]
                l[j-1] = tmp
        print('round done')
    return l

if __name__ == '__main__':
    input_list = [5, 9, 3, 1, 2, 8, 4, 7, 6]

    # sorted_list = bubble_sort_RTL(input_list)
    # sorted_list = selection_sort_RTL(input_list)
    sorted_list = selection_sort_LTR(input_list)

    assert sorted_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]
