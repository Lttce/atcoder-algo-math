# 017 - Least Common Multiple of N Integers

from numpy import lcm


def main():
    _ = int(input())
    print(lcm.reduce(list(map(int, input().split()))))


if __name__ == '__main__':
    main()
