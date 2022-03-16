# 015 - Greatest Common Divisor

from numpy import gcd


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == '__main__':
    main()
