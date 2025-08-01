import sys
import math

def main():
    sqrt337 = math.sqrt(337)
    readline = sys.stdin.readline

    while True:
        line = readline()
        if not line:
            break
        d, rh, rv = map(float, line.split())
        if d == rh == rv == 0.0:
            break

        hdpi = rh * sqrt337 / (16.0 * d)
        vdpi = rv * sqrt337 / (9.0 * d)

        print('Horizontal DPI: %.2f' % (hdpi))
        print('Vertical DPI: %.2f' % (vdpi))

if __name__ == '__main__':
    main()