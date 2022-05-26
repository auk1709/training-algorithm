import sys


def main(lines):
    place = []
    for i, v in enumerate(lines):
        if i == 0:
            N = int(v)
        if i > 0:
            place.append(list(map(int, v.split())))
    A = sorted([p[0] for p in place])
    B = sorted([p[1] for p in place])
    mid = len(place) // 2
    s = A[mid]
    g = B[mid]
    ans = 0
    for i in range(N):
        time = g - s
        if place[i][0] < s:
            time += 2*(s - place[i][0])
        if place[i][1] > g:
            time += 2*(place[i][1] - g)
        ans += time
    # print(f'{s}, {g}')
    print(ans)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
