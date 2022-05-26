from cmath import sqrt
import sys


def binary_search(sorted_array, target):
    left = 0
    right = len(sorted_array) - 1
    while left <= right:
        mid = left + ((right - left) // 2)
        # print(f'left: {left},mid: {mid}, right: {right}')
        if sorted_array[mid] == target:
            return mid
        elif sorted_array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def main(lines):
    column = []
    for i, v in enumerate(lines):
        if i == 0:
            n = int(v)
        else:
            column.append(tuple(map(int, v.split())))
    ans = 0
    column.sort()
    column_set = set(column)
    for i in range(n-1):
        for j in range(i+1, n):
            q = (column[j][0] - column[j][1] + column[i][1],
                 column[j][1] + column[j][0] - column[i][0])
            r = (column[i][0] - column[j][1] + column[i][1],
                 column[i][1] + column[j][0] - column[i][0])
            if q in column_set and r in column_set:
                ans = max(ans, (column[i][0] - column[j][0])
                          ** 2 + (column[i][1] - column[j][1])**2)

    print(ans)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
