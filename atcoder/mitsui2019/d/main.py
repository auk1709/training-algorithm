import sys


def main(lines):
    for i, v in enumerate(lines):
        if i == 0:
            N = int(v)
        if i == 1:
            S = v
    ans = 0
    for i in range(1000):
        s = f'{i:03}'
        cur = 0
        for j in range(N):
            if s[cur] == S[j]:
                if cur == 2:
                    ans += 1
                    break
                else:
                    cur += 1
    print(ans)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
