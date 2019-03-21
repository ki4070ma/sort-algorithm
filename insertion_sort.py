
def insertion_sort_RTL(l):
    length = len(l)
    for i in range(1, length):  # idx for target
        print('round start')
        for j in range(i-1, -1, -1):  # idx to replace with target
            if l[i] > l[j]:  # Could find insertion position
                # print('Found insertion pos')
                val = l[i]
                l.remove(val)
                num = length - len(l)
                for k in range(num):
                    l.insert(j + 1, val)
                break

            if j == 0:  # Couldn't find insertion position
                # print('Not found insertion pos')
                val = l[i]
                l.remove(val)
                num = length - len(l)
                for k in range(num):
                    l.insert(0, val)
        print(l)
    return l


if __name__ == '__main__':
    input_list = [5, 9, 3, 1, 2, 8, 4, 7, 6]

    sorted_list = insertion_sort_RTL(input_list)

    assert sorted_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]
