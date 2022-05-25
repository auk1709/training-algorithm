import sys


def main(lines):
    A = []
    for i, v in enumerate(lines):
        if i == 0:
            N, M = map(int, v.split())
        if i > 0:
            A.append(list(map(int, v.split())))

    ans = 0
    for i in range(M-1):
        for j in range(i, M):
            point = 0
            for k in range(N):
                point += max(A[k][i], A[k][j])
            ans = max(ans, point)
    print(ans)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
