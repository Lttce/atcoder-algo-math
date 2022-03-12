from sys import stdin
import numpy as np


def main():
    input = stdin.readline

    print(np.prod(list(map(int, input().split()))))


if __name__ == '__main__':
    main()
