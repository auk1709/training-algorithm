import sys


def main(lines):
    for i, v in enumerate(lines):
        if i == 0:
            N = int(v)
        if i == 1:
            heights = list(map(int, v.split()))

    dp = [10 ** 10] * N

    dp[0] = 0
    dp[1] = abs(heights[1] - heights[0])

    for i in range(2, N):
        dp[i] = min(dp[i-2] + abs(heights[i] - heights[i-2]),
                    dp[i-1] + abs(heights[i] - heights[i-1]))
    print(dp[N-1])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
