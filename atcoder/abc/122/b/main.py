import sys


def main(lines):
    for i, v in enumerate(lines):
        S = v
    ans = 0
    for i in range(0, len(S)):
        for j in range(i+1, len(S)+1):
            partial = S[i:j]
            length = len(partial)
            for p in partial:
                if p != 'A' and p != 'C' and p != 'T' and p != 'G':
                    length = 0
                    break
            ans = max(ans, length)
    print(ans)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
