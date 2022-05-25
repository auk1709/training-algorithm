import sys


def main(lines):
    for i, v in enumerate(lines):
        N = int(v)

    ans = 0
    for i in range(1, N+1, 2):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count == 8:
            ans += 1
    print(ans)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
