# 016 - Greatest Common Divisor of N Integers

from numpy import gcd


def main():
    _ = int(input())
    print(gcd.reduce(list(map(int, input().split()))))


if __name__ == '__main__':
    main()
