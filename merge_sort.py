

def merge_sort(l):
    center = int(len(l) / 2)
    array = l
    if center > 0:
        left = merge_sort(l[:center])
        right = merge_sort(l[center:])
        array = []
        while len(left) != 0 or len(right) != 0:
            print('start')
            print('left: {}'.format(left))
            print('right: {}'.format(right))
            if len(left) == 0 and len(right) != 0:
                array.append(right.pop(0))
            elif len(left) != 0 and len(right) == 0:
                array.append((left.pop(0)))
            elif left[0] < right[0]:
                array.append(left.pop(0))
            else:
                array.append(right.pop(0))
            print('left: {}'.format(left))
            print('right: {}'.format(right))
    print(array)
    return array




if __name__ == '__main__':
    input_list = [5, 9, 3, 1, 2, 8, 4, 7, 6]

    sorted_list = merge_sort(input_list)

    assert sorted_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]
