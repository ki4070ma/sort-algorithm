
# Left to Right, find maximum
def bubble_sort_LTR(l):
    length = len(l)
    for i in range(0, length-1):  # TODO Hard to understand around idx
        for j in range(0, length-1-i):
            print(l)
            if l[j] > l[j+1]:
                tmp = l[j]
                l[j] = l[j+1]
                l[j+1] = tmp
        print('round done')
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
    sorted_list = bubble_sort_LTR(input_list)

    assert sorted_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]
