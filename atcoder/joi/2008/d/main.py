import sys


def main(lines):
    target = []
    image = []
    for i, v in enumerate(lines):
        if i == 0:
            m = int(v)
        if i > 0 and i <= m:
            target.append(tuple(map(int, v.split())))
        if i == m+1:
            n = int(v)
        if i > m+1:
            image.append(tuple(map(int, v.split())))
    img_set = set(image)
    for i in range(n):
        dx = image[i][0] - target[0][0]
        dy = image[i][1] - target[0][1]
        for j in range(m):
            if (target[j][0] + dx, target[j][1] + dy) not in img_set:
                break
            if j == m - 1:
                print(f'{dx} {dy}')
                return


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
