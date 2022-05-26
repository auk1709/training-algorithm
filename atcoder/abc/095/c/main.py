import sys


def main(lines):
    for i, v in enumerate(lines):
        A, B, C, X, Y = map(int, v.split())
    ans = (A*X) + (B*Y)
    if(X > Y):
        ans = min(ans, 2*C*X)
        ans = min(ans, 2*C*Y + (X-Y)*A)
    else:
        ans = min(ans, 2*C*Y)
        ans = min(ans, 2*C*X + (Y-X)*B)
    print(ans)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
